from django.shortcuts import render, get_object_or_404
from .models import Course, Subject, Content
from django.views.generic import ListView
from django.http import HttpRequest


class IndexView(ListView):
    template_name = 'upskill/index.html'
    context_object_name = 'subjects'
    
    def get_queryset(self):
        subjects = Subject.objects.all()
        return subjects


def course(request, subject_slug):
    if subject_slug:
        courses = Course.objects.filter(slug=subject_slug)
    else:
        courses = Course.objects.all()
    
    content = {
        'courses': courses.order_by('id'),
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