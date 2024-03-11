from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from academy.repositories import PromotionRepository, CourseRepository
from common.repositories import ImageRepository
from common.schemas import ImageSchema, MetaSchema, TechnologySchema
from .schemas import PromotionSchema, CourseSchema
from .service import CourseService


@require_http_methods(["GET"])
def get_academy_courses(request):
    course_repo = CourseRepository()
    courses = course_repo.get_all()
    paginator = Paginator(courses, 2)
    page_num = request.GET.get('page')
    data = []
    for model in paginator.get_page(page_num).object_list:
        schema = CourseSchema.model_validate(model).model_dump()
        schema['image'] = ImageSchema.model_validate(model.image).model_dump()
        schema['meta'] = MetaSchema.model_validate(model.meta).model_dump()
        schema['tech_and_solution'] = [TechnologySchema.model_validate(tech).model_dump() for tech in
                                       model.tech_and_solution.all()]
        data.append(schema)
    return JsonResponse({"result": data})


@require_http_methods(["GET"])
def get_academy_course(request, course_id):
    course_repo = CourseRepository()
    course = course_repo.get_single(id=course_id)
    if course is None:
        return JsonResponse({}, status=400)
    course_as_dict = CourseSchema.model_validate(course).model_dump()
    course_as_dict['image'] = ImageSchema.model_validate(course.image).model_dump()
    course_as_dict['meta'] = MetaSchema.model_validate(course.meta).model_dump()
    course_as_dict['tech_and_solutions'] = [TechnologySchema.model_validate(tech).model_dump() for tech in
                                            course.tech_and_solution.all()]
    return JsonResponse(course_as_dict, status=200)


@require_http_methods(["GET"])
def get_academy_promotions(request):
    promotion_repo = PromotionRepository()
    promotions = promotion_repo.get_all()
    paginator = Paginator(promotions, 2)
    page_num = request.GET.get('page')
    data = []
    for model in paginator.get_page(page_num).object_list:
        model_schema = PromotionSchema.model_validate(model).model_dump()
        model_schema['image'] = ImageSchema.model_validate(model.image).model_dump()
        model_schema['meta'] = MetaSchema.model_validate(model.meta).model_dump()
        model_schema['courses'] = [CourseSchema.model_validate(course).model_dump() for course in model.course.all()]
        data.append(model_schema)
    return JsonResponse({'result': data}, status=200)


@require_http_methods(["GET"])
def get_academy_promotion(request, promotion_id):
    promotion_repo = PromotionRepository()
    promotion = promotion_repo.get_single(id=promotion_id)
    if promotion is None:
        return JsonResponse({}, status=404)
    promotion_schema = PromotionSchema.model_validate(promotion).model_dump()
    promotion_schema['image'] = ImageSchema.model_validate(promotion.image).model_dump()
    promotion_schema['meta'] = MetaSchema.model_validate(promotion.meta).model_dump()
    promotion_schema['courses'] = [CourseSchema.model_validate(course).model_dump() for course in
                                   promotion.course.all()]
    return JsonResponse(promotion_schema, status=200)


@require_http_methods(["GET"])
def test(req):
    return JsonResponse({'string': 'test'}, status=200)
