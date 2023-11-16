from django.contrib import admin
from .models import UserInfo, UserAddress
# Register your models here.

@admin.register(UserInfo)
class UserInfoadmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone','created_at']
    # ordering = ['id']

@admin.register(UserAddress)
class UserAddressadmin(admin.ModelAdmin):
    list_display = ['id','phone','pin_code','State','district','created_at']
    ordering = ['id']


