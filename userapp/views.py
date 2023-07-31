from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

<<<<<<< HEAD
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
        print(serializer)
=======
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
>>>>>>> 22a1c3f32b05e8278ed77c5a50b86f5b0c7f8408
        if serializer.is_valid():
            print('jjjjjjjjjj',serializer)
            serializer.save()
<<<<<<< HEAD
            res = {'messages': 'Data create successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            
=======
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
>>>>>>> 22a1c3f32b05e8278ed77c5a50b86f5b0c7f8408

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=204)