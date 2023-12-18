from django.db.models import QuerySet
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from academy.repositories import PromotionRepository, CourseRepository
from .schemas import PromotionSchema, CourseSchema


@require_http_methods(["GET"])
def get_academy_courses(request):
    course_repo = CourseRepository()
    courses = course_repo.get_values_list()
    paginator = Paginator(courses, 2)
    page_num = request.GET.get('page')
    data = [CourseSchema.model_validate(schema).model_dump() for schema in paginator.get_page(page_num)]
    return JsonResponse({"result": data})


@require_http_methods(["GET"])
def get_academy_course(request, course_id):
    course_repo = CourseRepository()
    course_qs: QuerySet = course_repo.get_all().filter(id=course_id)
    if course_qs.exists():
        course = course_qs.first()
        return JsonResponse(CourseSchema(
            name=course.name,
            discount=course.discount,
            price=course.price,
            block_content=course.block_content
        ).model_dump(), status=200)
    raise Http404


@require_http_methods(["GET"])
def get_academy_promotions(request):
    promotion_repo = PromotionRepository()
    promotions = promotion_repo.get_all()
    paginator = Paginator(promotions, 2)
    page_num = request.GET.get('page')
    data = [PromotionSchema(
        name=promotion.name,
        dt_start=promotion.dt_start,
        dt_end=promotion.dt_end,
        block_content=promotion.block_content
    ).model_dump() for promotion in paginator.get_page(page_num)]
    return JsonResponse({'result': data}, status=200)


@require_http_methods(["GET"])
def get_academy_promotion(request, promotion_id):
    promotion_repo = PromotionRepository()
    promotion_qs = promotion_repo.get_all().filter(id=promotion_id)
    if promotion_qs.exists():
        promotion = promotion_qs.first()
        return JsonResponse(PromotionSchema(
            name=promotion.name,
            dt_start=promotion.dt_start,
            dt_end=promotion.dt_end,
            block_content=promotion.block_content
        ).model_dump(), status=200)
    raise Http404
