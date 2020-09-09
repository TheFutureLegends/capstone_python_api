from django.urls import path, include
from auth_app import views

urlpatterns = [
    path("", include('djoser.urls')),
    path("", include('djoser.urls.jwt'))
]

# /auth/users/ -> register new user in auth_user table
#### Params: username, email, password

# /auth/jwt/create/ -> get new JWT for user
#### Params: username, password
#### Response: {access: <string>, refresh: <string>}

# /auth/users/me/ -> get current authenticated user
#### Headers: Bearer + access
#### Response: {username: "", email: "", id: <int>} 