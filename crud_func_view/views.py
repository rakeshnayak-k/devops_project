from django.shortcuts import render
import json
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        # json_data = request.body
        # stream = io.BytesIO(json_data)
        # python_data = JSONParser().parse(stream)
        # string_data = stream.decode('utf-8')
        # python_data = json.loads(string_data)
        # in_id = python_data.get('id',None)
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            in_id = json_data.get('id',None)
            if in_id is not None:
                stu = Student.objects.get(roll=in_id)
                serializer = StudentSerializer(stu)
                # json_data = JSONRenderer().render(serializer.data)
                # return HttpResponse(json_data, content_type='application/json')
                return JsonResponse(serializer.data,safe=False)
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            # json_data = JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(serializer.data,safe=False)
        except Exception as e:
            res = {'error msg': str(e)}
            res_json = JSONRenderer().render(res)
            return HttpResponse(res_json, content_type='application/json')
      
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            stu = Student.objects.filter(roll=json_data.get("roll"))
            if not stu.exists():
                serializer = StudentSerializer(data=json_data)
                if serializer.is_valid():
                    serializer.save()
                    res = {'msg': 'Student Created'}
                    json_data1 = JSONRenderer().render(res)
                    return HttpResponse(json_data1, content_type='application/json')
                json_data1 = JSONRenderer().render(serializer.errors)
                return HttpResponse(json_data1, content_type='application/json')
            res1 = {'msg': 'Student already Exits'}
            user_exit = JSONRenderer().render(res1)
            return HttpResponse(user_exit, content_type='application/json')
        except Exception as e:
            res = {'error msg': str(e)}
            res_json = JSONRenderer().render(res)
            return HttpResponse(res_json, content_type='application/json')
        
    if request.method == 'PUT':
        try:
            python_data = json.loads(request.body.decode('utf-8')) # loads() json data(request.body) to python data
            stu = Student.objects.get(roll=python_data.get("roll"))
            serializer = StudentSerializer(stu, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Student Updated Sucessfully'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            json_error = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_error, content_type='application/json')
        except Exception as e:
            res = {'error msg': str(e)}
            res_json = JSONRenderer().render(res)
            return HttpResponse(res_json, content_type='application/json')








        



