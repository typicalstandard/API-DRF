# link_manager/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/drf-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
]
