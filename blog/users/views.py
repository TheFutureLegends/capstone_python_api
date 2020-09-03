from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Users
from .api.serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(["GET", "POST"])
def user_list(request):
    if request.method == "GET":
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def user_detail(request, id):
    try:
        user = Users.objects.get(pk=id)
    except Users.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UsersSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = UsersSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)