from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path('stu-info-cbv/',StudentAPIView.as_view(), name='stu-info-cbv'),
]
