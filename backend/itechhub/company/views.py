import json
from django.http import HttpResponse, JsonResponse, Http404
from .models import CompanyService, CompanyCase, Company
from django.views.decorators.http import require_http_methods
from common.models import Image, Meta
from django.views import View
from django.core.paginator import Paginator


def get_company_services(request):
    company_services = list(CompanyService.objects.all())
    paginator = Paginator(company_services, 2)
    page_num = request.GET.get('page')
    data = []
    for service in paginator.get_page(page_num).object_list:
        service_object = {
            'name': service.name,
            'order_number': service.order_number,
            'image_id': service.image_id,
            'block_content': service.block_content
        }
        data.append(service_object)
    return JsonResponse({"result": data})


def get_company_service(request, service_id, **kwargs):
    if CompanyService.objects.filter(id=service_id).exists():
        return JsonResponse(CompanyService.objects.filter(id=service_id).values()[0], status=200)
    else:
        raise Http404


def get_company_cases(request):
    if request.method == "GET":
        company_cases = list(CompanyCase.objects.all())
        paginator = Paginator(company_cases, 2)
        page_num = request.GET.get('page')
        print(page_num)
        data = []
        print(paginator.get_page(page_num).object_list)
        for case in paginator.get_page(page_num).object_list:
            case_object = {
                'title': case.title,
                'order_number': case.order_number,
                'image_id': case.image_id,
                'block_content': case.block_content,
                'meta_id': case.meta_id,
                'company_id': case.company_id,
            }
            data.append(case_object)
        return JsonResponse({'result': data})
    if request.method == "POST":
        request_data = json.loads(request.body)

        image = Image()
        image.path = "path"

        image.save()

        company = Company()
        company.name = "itechhub"
        company.image = image
        company.block_content = {}

        company.save()

        meta = Meta()
        meta.title = "title"
        meta.description = "description"
        meta.h1_title = "h1_title"
        meta.seo_image = image

        meta.save()

        company_case = CompanyCase()
        company_case.title = request_data["title"]
        company_case.company = company
        company_case.block_content = {}
        company_case.order_number = request_data["order_number"]
        company_case.meta = meta
        company_case.image = image

        company_case.save()
        return JsonResponse({"result": request_data})


def get_company_case(request, case_id):
    if CompanyCase.objects.filter(id=case_id).exists():
        return JsonResponse(CompanyCase.objects.filter(id=case_id).values()[0])
    else:
        raise Http404
