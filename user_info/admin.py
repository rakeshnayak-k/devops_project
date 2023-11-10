from django.contrib import admin
from .models import UserInfo
# Register your models here.

class UserInfoadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone','created_at']

admin.site.register(UserInfo,UserInfoadmin)
