from django.urls import path
from posts_comments.views import comment_list, comment_detail, reply_list, reply_detail

urlpatterns = [
    # comment
    path('api/post/<slug:slug>/comments/', comment_list),
    path('api/post/comment/<int:id>/', comment_detail),
    # replies of comment
    path('api/post/<slug:post_slug>/comment/<int:comment_id>/replies/', reply_list),
    path('api/post/<slug:post_slug>/comment/<int:comment_id>/replies/<int:reply_id>/', reply_detail),
]