from django.urls import path
from . import views

urlpatterns = [
    path('user-info/', views.user_info_form, name='user_info_form'),
    path('user-create/', views.user_create, name='user-create'),
]
