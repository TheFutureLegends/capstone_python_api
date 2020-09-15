from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from blog.posts.models import Posts
from blog.posts.api.serializers import PostsSerializer
from .models import PostComments
from .api.serializers import PostCommentsSerializer

# Create your views here.
@api_view(["GET", "POST"])
def comment_list(request, slug):
    # Filter and get first post with exact slug
    try:
        post = Posts.objects.get(slug=slug)
    except Posts.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Filter comment that has post_id same as post.id
    # Parent_id should be null as this is a comment, not reply
    try:
        comments = PostComments.objects.filter(
            post_id=post.id,
            parent_id__isnull=True
        )
    except PostComments.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PostCommentsSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        # if request.data.get('parent_id'):
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = PostCommentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED);

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def comment_detail(request, id):
    
    # Get specific comment with pk = id params
    # Parent_id should be null as this is a comment, not reply
    try:
        comment = PostComments.objects.get(
            pk=id,
            parent_id__isnull=True
        )
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostCommentsSerializer(comment)
        return Response(serializer.data)

    elif request.method == "PUT":
        # if request.data.get('parent_id'):
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = PostCommentsSerializer(comment, data=request.data)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        comment.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def reply_list(request, post_slug, comment_id):
    # Filter and get first post with exact slug
    try:
        post = Posts.objects.get(slug=post_slug)
    except Posts.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Filter replies based on post slug and comment id
    try:
        replies = PostComments.objects.filter(
            post_id=post.id,
            parent_id=comment_id
        )
    except PostComments.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Checking method of request
    if request.method == "GET":
        serializer = PostCommentsSerializer(replies, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        if request.data.get('parent_id'):
            serializer = PostCommentsSerializer(data=request.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def reply_detail(request, post_slug, comment_id, reply_id):
    # Filter and get first post with exact slug
    try:
        post = Posts.objects.get(slug=post_slug)
    except Posts.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Filter replies based on post slug and comment id
    try:
        reply = PostComments.objects.get(
            pk=reply_id,
            post_id=post.id,
            parent_id=comment_id
        )
    except PostComments.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostCommentsSerializer(reply)
        return Response(serializer.data)
    elif request.method == "PUT":
        if request.data.get('parent_id'):
            serializer = PostCommentsSerializer(reply, data=request.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data);
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        reply.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)