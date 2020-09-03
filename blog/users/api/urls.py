from django.urls import path
from users.views import user_list, user_detail

urlpatterns = [
    path('api/users/', user_list),
    path('api/users/<int:id>/', user_detail),
]