from django.views import View
from django.shortcuts import render
from academy.repositories import CourseRepository


class CourseListAdminView(View):
    repository = CourseRepository

    def get(self):
