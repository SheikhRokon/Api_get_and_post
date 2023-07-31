from django.urls import path
from test1 import views


urlpatterns = [
    path('studentapi',views.hello_world),
]