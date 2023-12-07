import json
from django.http import HttpResponse, JsonResponse
from .models import CompanyService
from django.views.decorators.http import require_http_methods
from common.models import Image
from django.views import View


class CompanyView(View):
    def post(self, request):
        company_service = CompanyService()

        body = request.body

        data = json.loads(body.decode("utf-8"))

        image = Image()

        image.path = data["image"]["path"]

        image.save()

        company_service.name = data["name"]
        company_service.block_content = data["block_content"]
        company_service.order_number = data["order_number"]
        company_service.image = image

        company_service.save()
        return HttpResponse(body, status=201)

    def get(self, request, test_id):
        print(test_id)
        return JsonResponse({'results': list(CompanyService.objects.values())}, status=200)

