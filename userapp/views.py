from django.shortcuts import render
from .models import *

# Api get import
import requests

#Api post import
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse



# Api get
appKey = 'http://127.0.0.1:8000/bbb'

def home(request):
    url = f'{appKey}'
    response = requests.get(url)
    data = response.json()
    # print(data)
    context={
        'data':data
    }
    return render(request,'userapp/home.html',context)



#Api post
def student_details(request):
    stu = Student.objects.get(id=1)
    Serializer = StudentSerializers(stu)
    json_data = JSONRenderer().render(Serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def student_list(request):
    stu = Student.objects.all()
    Serializer = StudentSerializers(stu ,many=True)
    json_data = JSONRenderer().render(Serializer.data)
    return HttpResponse(json_data, content_type='application/json')

   