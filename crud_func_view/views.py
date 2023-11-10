from django.shortcuts import render
import json
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser


# Create your views here.

def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        # python_data = JSONParser().parse(stream)
        string_data = stream.decode('utf-8')
        python_data = json.loads(string_data)
        # json_data = json.loads(request.body.decode('utf-8'))
        in_id = python_data.get('id',None)
        if in_id is not None:
            stu = Student.objects.get(roll=in_id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data,safe=False)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
        



