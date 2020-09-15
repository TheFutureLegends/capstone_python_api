from django.db import models
from blog.posts.models import Posts


# Create your models here.
class PostComments(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150, unique=False, null=False)
    post_id = models.ForeignKey(Posts, related_name="post_id", on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', related_name="comment_parent", null=True, blank=True,
                                  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'post_comments'

    def __str__(self):
        return self.content
