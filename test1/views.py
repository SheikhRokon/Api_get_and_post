from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view()
# def hello_world(request):
#     return Response({'view':'RokongWorld'})


@api_view([ 'GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'view':'This is a GET request'})
        
    if request.method=='POST':
        return Response({'view':'This is a POST request','success':request.data})
    