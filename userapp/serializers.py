from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    father_name = serializers.CharField(max_length=100)
    roll = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    

def create(self, validate_data):
    return Student.objects.create(**validate_data)


    

    
