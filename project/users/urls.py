from django.urls import path
from .views import RegisterView, ChangePasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('change-password/', ChangePasswordView.as_view(),name='change_password'),
]
