from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Showcases
from .api.serializers import ShowcaseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(["GET", "POST"])
def showcase_list(request):
    if request.method == "GET":
        showcases = Showcases.objects.all()

        serializer = ShowcaseSerializer(showcases, many=True)
        
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ShowcaseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def showcase_detail(request, slug):
    try:
        showcases = Showcases.objects.get(slug=slug)
    except Showcases.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ShowcaseSerializer(showcases)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ShowcaseSerializer(showcases, data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        showcases.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)