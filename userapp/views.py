from django.shortcuts import render
from .models import *

# Api get import
import requests

#Api post import
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse ,JsonResponse




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
    # json_data = JSONRenderer().render(Serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(Serializer.data, safe=False)
    return JsonResponse(Serializer.data, safe= False)



import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream =io.BytesIO(json_data)                #Converting json data to stream data. জেসন ডাটাকে স্ট্রিম ডাটাতে রূপান্তর
        pythondata = JSONParser().parse(stream)         #Convert stream data to Python data স্ট্রিম ডাটাকে পাইথন  ডাটাতে রূপান্তর 
        serializer = StudentSerializers(data=pythondata)         #Convert Python data to complex data পাইথন ডাটাকে কমপ্লেক্স ডাটাতে রূপান্তর
        if serializer.is_valid():
            serializer.save()
            res = {'messages': 'Data create successfully'}
            json_data = JsonResponse().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
            


   