from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json


# Create your views here.

def user_info_form(request):
    try:
        obj = UserInfo.objects.all()
        serializer = UserInfoSerializer(obj,many=True)
        json_data = JSONRenderer().render(serializer.data)
        # use JsonResponse it is short andd good
        # return JsonResponse(serializer.data,safe=False)
        return HttpResponse(json_data, content_type='application/json')
    except Exception as e:
        res = {'error msg': str(e)}
        res_json = JSONRenderer().render(res)
        return HttpResponse(res_json, content_type='application/json')


# @api_view(['POST'])
@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        try:
            # json_data = request.body
            json_data = json.loads(request.body.decode('utf-8'))
            obj = UserInfo.objects.filter(email=json_data.get("email"))
            if not obj.exists():
                # stream = io.BytesIO(json_data)
                # python_data = JSONParser().parse(json_data)
                serializer = UserInfoSerializer(data=json_data)
                if serializer.is_valid():
                    serializer.save()
                    res = {'msg': 'User Created'}
                    json_data1 = JSONRenderer().render(res)
                    return HttpResponse(json_data1, content_type='application/json')
                json_error = JSONRenderer().render(serializer.errors)
                return HttpResponse(json_error, content_type='application/json')
            res1 = {'msg': 'User already Exits'}
            user_exit = JSONRenderer().render(res1)
            return HttpResponse(user_exit, content_type='application/json')
        except Exception as e:
            res = {'error msg': str(e)}
            res_json = JSONRenderer().render(res)
            return HttpResponse(res_json, content_type='application/json')




    




