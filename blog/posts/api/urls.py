from django.urls import path
from posts.views import post_list, post_detail, post_store, post_update, get_popular_post, get_slider_posts, get_latest_posts, get_blog_paginate

urlpatterns = [
    path('api/posts/', post_list),
    path('api/post/<slug:slug>/', post_detail),
    path('api/post/store', post_store),
    path('api/post/<slug:slug>/update', post_update),
    
    path('api/posts/paginator/', get_blog_paginate),
    path('api/posts/latest/', get_latest_posts),
    path('api/posts/popular/', get_popular_post),
    path('api/posts/slider/', get_slider_posts),
]