from django.urls import path
from posts.views import post_list, post_detail, get_popular_post, get_slider_posts, get_latest_posts, get_blog_paginate

urlpatterns = [
    path('api/posts/', post_list),
    path('api/posts/paginator/', get_blog_paginate),
    path('api/posts/latest/', get_latest_posts),
    path('api/posts/popular/', get_popular_post),
    path('api/posts/slider/', get_slider_posts),
    path('api/post/<slug:slug>/', post_detail),
]