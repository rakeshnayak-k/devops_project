from rest_framework import serializers
from .models import UserInfo, UserAddress


class UserInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)

    def create(self,validate_data):
        return UserInfo.objects.create(**validate_data)

class UserAddressSerializer(serializers.ModelSerializer):
    # phone = UserInfoSerializer()
    pin_code = serializers.CharField(read_only=True) # read_only for a single field 
    class Meta:
        model = UserAddress
        fields = '__all__'
        # fields = ['phone','pin_code','State','district']     
        # read_only = ['pin_code','state'] # read_only for multiple fields
