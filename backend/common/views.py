from django.shortcuts import render
from django.http import HttpResponse


def index(request, question_id):
    return HttpResponse(f"work! {question_id}")
