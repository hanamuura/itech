import json
from dataclasses import asdict
from django.http import JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from .models import *
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
    course = course_repo.get_all().filter(id=course_id)
    print(course)
    if course.exists():
        course_schema = CourseSchema.model_validate(course).model_loads()
        print(course_schema)
        return JsonResponse(CourseSchema.model_validate(course).model_dump(), status=200)
    raise Http404


@require_http_methods(["GET"])
def get_academy_promotions(request):
    promotion_repo = PromotionRepository()
    promotions = promotion_repo.get_values_list()
    paginator = Paginator(promotions, 2)
    page_num = request.GET.get('page')
    data = [PromotionSchema.model_validate(promotion) for promotion in paginator.get_page(page_num)]
    return JsonResponse({'result': list(data)}, status=200)


@require_http_methods(["GET"])
def get_academy_promotion(request, promotion_id):
    promotion = Promotion.objects.filter(id=promotion_id)
    if promotion.exists():
        return JsonResponse(promotion.values()[0], status=200)
    raise Http404
