from django.urls import path
from .views import todo_list, todo_detail

urlpatterns = [
<<<<<<< HEAD
   path('',home,name='home'),
   path('aaa',student_details,name='aaa'),
   path('bbb',student_list,name='bbb'),
   path('student_create/',student_create,name='student_create'),
   

=======
    path('todos/', todo_list, name='todo-list'),
    path('todos/<int:pk>/', todo_detail, name='todo-detail'),
>>>>>>> 22a1c3f32b05e8278ed77c5a50b86f5b0c7f8408
]