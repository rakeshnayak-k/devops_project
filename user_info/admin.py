from django.contrib import admin
from .models import UserInfo
# Register your models here.

@admin.register(UserInfo)
class UserInfoadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone','created_at']
    ordering = ['id']


