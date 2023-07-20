from rest_framework import serializers
from .models import *

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    father_name = serializers.CharField(max_length=100)
    roll = serializers.CharField(max_length=100)
    email = serializers.EmailField()

    
