from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


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
        
