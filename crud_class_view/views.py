from django.shortcuts import render
import json
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentAPIView(View):
    def get(self, request, *args, **kwargs):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            in_id = json_data.get('id',None)
            if in_id is not None:
                stu = Student.objects.get(roll=in_id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data,safe=False)
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many=True)
            return JsonResponse(serializer.data,safe=False)
        except Exception as e:
            res = {'error msg': str(e)}
            res_json = JSONRenderer().render(res)
            return HttpResponse(res_json, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
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
        
    def put(self, request, *args, **kwargs):
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
        
    def delete(self, request, *args, **kwargs):
        try:
            python_data = json.loads(request.body.decode('utf-8')) # loads() json data(request.body) to python data
            stu = Student.objects.get(roll=python_data.get("roll"))
            # we don't have to do validations for deleting a model object we ca delete it directly using delete() method
            stu.delete()
            res = {'msg': 'Student deleted Successfully'}
            res_del = JSONRenderer().render(res)
            return HttpResponse(res_del, content_type='application/json')
        except Exception as e:
            res = {'error msg': str(e)}
            res_json = JSONRenderer().render(res)
            return HttpResponse(res_json, content_type='application/json')