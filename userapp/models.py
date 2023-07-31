# todos/models.py
from django.db import models

<<<<<<< HEAD
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
=======
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
>>>>>>> 22a1c3f32b05e8278ed77c5a50b86f5b0c7f8408

    def __str__(self):
        return self.title


