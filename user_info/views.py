from django.shortcuts import render, HttpResponse
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.

def user_info_form(request):
    obj = UserInfo.objects.all()

    serializer = UserInfoSerializer(obj,many=True)

    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')
    




