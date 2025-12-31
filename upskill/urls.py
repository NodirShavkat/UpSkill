from django.urls import path 
from .views import IndexView, course, course_detail

app_name = "upskill"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('subject/<slug:subject_slug>', IndexView.as_view(), name='courses_of_subject'),
    path('course/', course, name='course'),
    path('course/detail/<slug:slug>', course_detail, name='detail'),
]
