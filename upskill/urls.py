from django.urls import path 
from .views import index, course

app_name = 'upskill'

urlpatterns = [
    path('', index, name='index'),
    path('course/', course, name='course'),
]