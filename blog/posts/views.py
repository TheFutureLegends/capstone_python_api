from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Posts
from .api.serializers import PostsSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from rest_framework.permissions import IsAuthenticated
import json


# Create your views here.
@api_view(["GET"])
def get_slider_posts(request):
    if request.method == "GET":
        posts = Posts.objects.order_by('?')[:3]
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_latest_posts(request):
    if request.method == "GET":
        posts = Posts.objects.order_by('-created_date')[:3]

        serializer = PostsSerializer(posts, many=True)

        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_blog_paginate(request):
    if request.method == "GET":
        posts = Posts.objects.order_by('-created_date')

        paginator = PageNumberPagination()

        paginator.page_size = 10

        result_page = paginator.paginate_queryset(posts, request=request)

        serializer = PostsSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_popular_post(request):
    if request.method == "GET":
        # adding '-' in field will sort descending
        posts = Posts.objects.all().order_by('-visit')[:3]
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def post_list(request):
    if request.method == "GET":
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def post_detail(request, slug):
    try:
        post = Posts.objects.get(slug=slug)
    except Posts.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# For Admin
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_dataTable(request):
    posts = Posts.objects.filter(author_id=request.user.id).order_by('-created_date')

    serializer = PostsSerializer(posts, many=True)
    
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_edit(request, slug):
    if request.method == "GET":
        try:
            posts = Posts.objects.get(slug=slug, author_id=request.user.id)
        except Posts.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        serializer = PostsSerializer(posts, many=True)

        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def post_store(request):
    if request.method == "POST":
        serializer = PostsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_edit(request, slug):
    if request.method == "GET":
        try:
            post = Posts.objects.get(slug=slug, author_id=request.user.id)
        except Posts.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        serializer = PostsSerializer(post)
        
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def post_update(request, slug):
    try:
        post = Posts.objects.get(slug=slug, author_id=request.user.id)
    except Posts.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PostsSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def post_delete(request, slug):
    user = request.user.id

    try:
        post = Posts.objects.filter(slug=slug, author_id=user).first()
    except Posts.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        post.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_401_UNAUTHORIZED)
