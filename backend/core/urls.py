"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from common.views import index
from itechhub.company.views import get_company_services, get_company_service, get_company_cases, get_company_case
from itechhub.views import get_employees

urlpatterns = [
    path('test/<int:question_id>', index),
    path('technological-services', get_company_services),
    path('technological-services/<int:service_id>', get_company_service),
    path('cases', get_company_cases),
    path('cases/<int:case_id>', get_company_case),
    path('our-team', get_employees)
]
