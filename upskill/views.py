from django.shortcuts import render
from .models import Course


def index(request):
    return render(request, 'upskill/index.html')


def course(request):
    courses = Course.objecsts.all()
    return render(request, 'upskill/course.html')