from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
       

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.name

