from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User




@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        print(name, age)
        return Response({"name": name, "age": age})
    context ={
        'name':'Rokon',
        'age':'19'
    }
    return Response(context)
        

@api_view(['POST'])
def registetionApi(request):
    
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        if User.objects.filter(username=username).exists():
            return Response({'error':'username already exists'})
        
        if confirm_password != password:
            return Response({'error':'Passwords do not match!'})
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        return Response({'message': 'Account created successfully!'})
    else:
        return Response({'message': 'All fields are required!'})
        

# @api_view(['GET', 'POST'])
# def loginApi(request):
#     if request.method == 'POST':
#         username = request.data['username']
#         password = request.data['password']
#         if User.objects.filter(username=username).exists():
#             user = User.objects.get(username=username)
#             if user.check_password(password):
#                 return Response({'message': 'Successfully logged in!'})
#             else:
#                 return Response({'error': 'Invalid password!'})
#         else:
#             return Response({'error': 'Invalid username!'})