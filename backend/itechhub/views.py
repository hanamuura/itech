from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from .models import Employee
from django.http import JsonResponse

from .repository import EmployeeRepository
from .schemas import EmployeeSchema


@require_http_methods(["GET"])
def get_employees(request):
    employee_repo = EmployeeRepository()
    employees = employee_repo.get_all()
    paginator = Paginator(employees, 2)
    page_num = request.GET.get('page')
    data = [EmployeeSchema().model_validate(employee) for employee in paginator.get_page(page_num)]
    return JsonResponse({'result': data}, status=200)
