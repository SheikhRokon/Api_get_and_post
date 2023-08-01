from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from ApiProject.views import MyTokenObtainPairView

urlpatterns = [
   path('registetionApi/',registetionApi),
   path('create_user/',create_user),
   path('registetionApi/token/',MyTokenObtainPairView.as_view()),
   path('registetionApi/token/referstoken/',TokenRefreshView.as_view()),

]