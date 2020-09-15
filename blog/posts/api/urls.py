from django.urls import path
from blog.posts.views import post_list, post_detail, post_dataTable, post_store, post_edit, post_update, post_delete, get_popular_post, get_slider_posts, get_latest_posts, get_blog_paginate

urlpatterns = [
    path('api/posts/', post_list),
    path('api/post/<slug:slug>/', post_detail),
    path('api/posts/paginator/', get_blog_paginate),
    path('api/posts/latest/', get_latest_posts),
    path('api/posts/popular/', get_popular_post),
    path('api/posts/slider/', get_slider_posts),

    # For authenticated user
    path('api/posts/dataTable', post_dataTable),
    path('api/post/store', post_store),
    path('api/post/<slug:slug>/edit', post_edit),
    path('api/post/<slug:slug>/update', post_update),
    path('api/post/<slug:slug>/delete', post_delete),
]