from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Posts
from .api.serializers import PostsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from blog.pagination import CustomPagination
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

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

        paginator = Paginator(posts, 20)

        page = request.QUERY_PARAMS.get('page')
        try:
            posts_paginator = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts_paginator = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999),
            # deliver last page of results.
            posts_paginator = paginator.page(paginator.num_pages)

        serializer_context = {'request': request}
        serializer = PaginatedPostSerializer(users, context=serializer_context)
        return Response(serializer.data)
        pass
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_popular_post(request):
    if request.method == "GET":
        # adding '-' in field will sort descending
        posts = Posts.objects.all().order_by('-visit')[:3]
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PostsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, slug):
    try:
        post = Posts.objects.get(slug=slug)
    except Posts.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PostsSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        post.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)