from django.urls import path
from . import views

urlpatterns = [
    path('stu-info/', views.student_api, name='stu-info'),

]
