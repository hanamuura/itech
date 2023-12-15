from django.views.decorators.http import require_http_methods
from .models import Employee
from django.http import JsonResponse


@require_http_methods(["GET"])
def get_employees(request):
    return JsonResponse({})
