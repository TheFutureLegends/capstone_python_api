from django.urls import path
from showcases.views import showcase_list, showcase_detail

urlpatterns = [
    path('api/showcases/', showcase_list),
    path('api/showcases/<slug:slug>/', showcase_detail),
]