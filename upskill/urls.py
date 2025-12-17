from django.urls import path 
from .views import IndexView, course, course_detail

app_name = 'upskill'

urlpatterns = [
    # path('', index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('course/', course, name='course'),
    path('course/<slug:subject_slug>', course, name='course'),
    path('course/detail/<slug:slug>', course_detail, name='detail'),
]
