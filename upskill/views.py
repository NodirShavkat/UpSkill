from django.shortcuts import render, get_object_or_404
from .models import Course, Subject, Content


def index(request):
    return render(request, 'upskill/index.html')


def course(request):
    courses = Course.objects.all()

    content = {
        'courses': courses,
    }
    return render(request, 'upskill/course.html', content)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    related_courses = Course.objects.filter(subject=course.subject).exclude(pk=course.pk)[:3]
    all_subjects = Subject.objects.all()

    context = {
        'course': course,
        'related_courses': related_courses,
        'subjects': all_subjects,
    }
    return render(request, 'upskill/detail.html', context)