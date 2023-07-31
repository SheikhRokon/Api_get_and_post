from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
   path('registetionApi/',registetionApi),
   path('registetionApi/token/',TokenObtainPairView.as_view()),
   path('registetionApi/token/referstoken/',TokenRefreshView.as_view()),

]