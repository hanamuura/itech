from django.http import JsonResponse, Http404, HttpResponse
from .models import *
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator


@require_http_methods(["GET"])
def get_blogs(request):
    blogs = list(BlogPost.objects.all())
    paginator = Paginator(blogs, 2)
    page_num = request.GET.get('page')
    data = []
    for blog in paginator.get_page(page_num):
        blog_object = {
            'name': blog.name,
            'block-content': blog.block_content,
            'image_id': blog.image_id,
            'meta': blog.meta,
        }
        data.append(blog_object)
    return JsonResponse({'result': data}, status=200)


def get_category_blogs(request, category):
    category = BlogCategory.objects.filter(name=category)
    return HttpResponse(category.values('name'))
