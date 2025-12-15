from django.urls import path 
from .views import index, course, course_detail

app_name = 'upskill'

urlpatterns = [
    path('', index, name='index'),
    path('course/', course, name='course'),
    path('course/detail/<slug:slug>', course_detail, name='detail'),
]
