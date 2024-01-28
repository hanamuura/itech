from django.http import JsonResponse
from django.views import View

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
        data = request
