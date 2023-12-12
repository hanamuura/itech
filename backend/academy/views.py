from django.http import JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from .models import Course
from django.core.paginator import Paginator


@require_http_methods(["GET"])
def get_academy_courses(request):
    courses = list(Course.objects.all())
    paginator = Paginator(courses, 2)
    page_num = request.GET.get('page')
    data = []
    for course in paginator.get_page(page_num).object_list:
        course_object = {
            'name': course.name,
            'discount': course.discount,
            'price': course.price,
            'block_content': course.block_content,
            'image_id': course.image_id
        }
        data.append(course_object)
    return JsonResponse({"result": data})


@require_http_methods(["GET"])
def get_academy_course(request, course_id):
    course = Course.objects.filter(id=course_id)
    if course.exists():
        return JsonResponse(course.values()[0], status=200)
    raise Http404
