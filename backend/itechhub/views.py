from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse
from common.models import Image
import json


# Create your views here.
def get_employees(request):
    if request.method == "GET":
        return JsonResponse(
            {'result': list(Employee.objects.all().values('full_name', 'position', 'career_summary', 'image_id'))},
            status=200)
    if request.method == "POST":
        image = Image.objects.filter(id=1).first()

        employee = Employee()
        data = json.loads(request.body)

        employee.position = data['position']
        employee.image = image
        employee.career_summary = data['career_summary']
        employee.full_name = data['full_name']

        employee.save()

        return JsonResponse({'result': data}, status=200)
