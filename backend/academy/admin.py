from django.core.paginator import Paginator
from django.http import JsonResponse, Http404, HttpResponse
from django.views import View
import json

from pydantic import ValidationError

from academy.models import Course
from academy.repositories import CourseRepository
from academy.schemas import CourseSchema, PromotionSchema
from academy.service import CourseService
from common.models import Image, Technology
from common.schemas import ImageSchema, TechnologySchema, MetaSchema


class AdminCourse(View):
    @classmethod
    def get(cls, request):
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

    @classmethod
    def post(cls, request):
        data = json.loads(request.body)
        try:
            image = data['image']
            technologies = data['tech_and_solution']
            technology_images = [tech['image'] for tech in technologies]

            course_schema = CourseSchema.model_validate(data).model_dump()
            technologies_schemas = [TechnologySchema.model_validate(tech).model_dump() for tech in technologies]
            technology_images_schemas = [ImageSchema.model_validate(image).model_dump() for image in technology_images]

            created_images = [Image.objects.create(**img) for img in technology_images_schemas]
            for i in range(len(created_images)):
                technologies_schemas[i]['image_id'] = created_images[i].id
            created_technologies = [Technology.objects.create(**tech) for tech in technologies_schemas]
            created_image = Image.objects.create(**image)
            course_schema['image_id'] = created_image.id
            course_schema['meta_id'] = 1
            created_course: Course = Course.objects.create(**course_schema)
            created_course.tech_and_solution.add(*created_technologies)

            return JsonResponse(data, status=200)
        except ValidationError:
            return HttpResponse("Incorrect input data", status=400)


class AdminSingleCourse(View):
    @classmethod
    def get(cls, request, course_id):
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

    @classmethod
    def patch(cls, request, course_id):
        data = json.loads(request.body)
        new_data = CourseService().patch(data, course_id)
        if new_data == {}:
            return JsonResponse({'error': 'ValidationError'}, status=400)
        return JsonResponse(new_data, status=200)
