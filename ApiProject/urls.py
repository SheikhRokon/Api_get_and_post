
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userapp.urls')),
<<<<<<< HEAD
    path('api-auth/', include('rest_framework.urls')),
    path('', include('registration.urls')),
=======
    path('', include('test1.urls')),
>>>>>>> 22a1c3f32b05e8278ed77c5a50b86f5b0c7f8408
]
