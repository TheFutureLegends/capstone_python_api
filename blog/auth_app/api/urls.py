from django.urls import path, include
from auth_app import views

urlpatterns = [
    path("", include('djoser.urls')),
    path("", include('djoser.urls.jwt'))
]