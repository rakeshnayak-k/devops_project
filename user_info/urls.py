from django.urls import path
from .views import user_create, user_info_form, UserAddressAPIView

urlpatterns = [
    path('user-info/', user_info_form, name='user_info_form'),
    path('user-create/', user_create, name='user-create'),
    path('user-address/', UserAddressAPIView.as_view(), name='user-address'),
]
