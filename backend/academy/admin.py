from django.http import JsonResponse, Http404, HttpResponse
from django.views import View
import json

from pydantic import ValidationError

from academy.models import Course
from academy.repositories import CourseRepository
from academy.schemas import CourseSchema, PromotionSchema


class AdminCourse(View):
    @classmethod
    def get(cls, request):
        course_repo = CourseRepository().get_all()
        data = []
        for course in course_repo:
            res = CourseSchema.model_validate(course).model_dump()
            items = [PromotionSchema.model_validate(promotion).model_dump() for promotion in course.promotion_courses.all()]
            res['promotions'] = items
            data.append(res)
        return JsonResponse({'result': data}, status=200)

    @classmethod
    def post(cls, request):
        data = json.loads(request.body)
        try:
            CourseSchema.model_validate(data)
            Course.objects.create(**data)
            return JsonResponse(data, status=202)
        except ValidationError:
            return HttpResponse("Incorrect input data")
