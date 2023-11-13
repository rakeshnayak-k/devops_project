"""
URL configuration for devops_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

admin.site.site_header = "DevOps Admin"
admin.site.site_title = "DevOps Admin Portal"
admin.site.index_title = "Welcome to DevOps Researcher Portal"

# schema_view = get_schema_view(
#    openapi.Info(
#       title="DevOps API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.ourapp.com/policies/terms/",
#       contact=openapi.Contact(email="contact@devop.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('', include('user_info.urls')),
    path('', include('crud_func_view.urls')),
    path('', include('crud_class_view.urls')),
]
