from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Create your views here.


def go_home(request):
    json_data = '{"status":"success"}'
    return HttpResponse("<p>welcome to python rest api</p></br><a href='/admin'>admin login</a>", content_type='text/html')


def get_student_by_id(request, student_id):
    student_data = Student.objects.get(id=student_id)
    serializer_data = StudentSerializer(student_data)
    json_data = JSONRenderer().render(serializer_data.data)
    return HttpResponse(json_data, content_type='application/json')


def get_student_list(request):
    student_data = Student.objects.all()
    serializer_data = StudentSerializer(student_data, many=True)
    # json_data = JSONRenderer().render(serializer_data.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer_data.data, safe=False)