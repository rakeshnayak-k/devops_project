from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15,primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

class UserAddress(models.Model):
    pin_code = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    phone = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    



