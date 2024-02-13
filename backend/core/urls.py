"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewsSS
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from academy.admin import AdminCourse, AdminSingleCourse
from itechhub.company.views import *
from itechhub.views import get_employees
from academy.views import *
from academy.blog.views import *


urlpatterns = [
    path('technological-services', get_company_services),
    path('technological-services/<int:service_id>', get_company_service),

    path('cases', get_company_cases),
    path('cases/<int:case_id>', get_company_case),

    path('our-team', get_employees),

    path('academy/course', get_academy_courses),
    path('academy/course/<int:course_id>', get_academy_course),
    path('academy/blog', get_blogs),
    path('academy/blog/<str:category>', get_category_blogs),
    path('academy/promotion', get_academy_promotions),
    path('academy/promotion/<int:promotion_id>', get_academy_promotion),
    path('academy/blog/<str:category>/<int:blogpost_id>', get_blog),

    path('company/<int:company_id>', get_company),

    path('admin/course', AdminCourse.as_view()),
    path('admin/course/<int:course_id>', AdminSingleCourse.as_view()),
    path('test', test)
]

