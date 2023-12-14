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


@require_http_methods(["GET"])
def get_category_blogs(request, category):
    blog_category = BlogCategory.objects.filter(name=category).first()
    posts = list(blog_category.blog_post_category.all())
    paginator = Paginator(posts, 2)
    page_num = request.GET.get('page')
    data = []
    for post in paginator.get_page(page_num):
        post_obj = {
            'name': post.name,
            'block_content': post.block_content,
            'image_id': post.image_id,
            'meta_id': post.meta_id,
        }
        data.append(post_obj)
    return JsonResponse({'result': data}, status=200)


@require_http_methods("GET")
def get_blog(request, category, blogpost_id):
    blog_category = BlogCategory.objects.filter(name=category).first()
    post = blog_category.blog_post_category.filter(id=blogpost_id)
    if post.exists():
        return JsonResponse(post.values()[0], status=200)
    raise Http404
