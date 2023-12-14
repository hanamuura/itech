from django.http import JsonResponse, Http404
from .models import CompanyService, CompanyCase, Company
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator


@require_http_methods(["GET"])
def get_company_services(request):
    company_services = list(CompanyService.objects.all())
    paginator = Paginator(company_services, 2)
    page_num = request.GET.get('page')
    print(page_num)
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


@require_http_methods(["GET"])
def get_company_service(request, service_id, **kwargs):
    if CompanyService.objects.filter(id=service_id).exists():
        return JsonResponse(CompanyService.objects.filter(id=service_id).values()[0], status=200)
    raise Http404


@require_http_methods(["GET"])
def get_company_cases(request):
    company_cases = list(CompanyCase.objects.all())
    paginator = Paginator(company_cases, 2)
    page_num = request.GET.get('page')
    data = []
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


@require_http_methods(["GET"])
def get_company_case(request, case_id):
    if CompanyCase.objects.filter(id=case_id).exists():
        return JsonResponse(CompanyCase.objects.filter(id=case_id).values()[0])
    else:
        raise Http404


@require_http_methods(["GET"])
def get_company(request, company_id):
    company = Company.objects.filter(id=company_id)
    if company.exists():
        return JsonResponse(company.values()[0], status=200)
    raise Http404
