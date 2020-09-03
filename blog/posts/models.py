from django.db import models
from django.db.models.signals import pre_save

from blog.utils import unique_slug_generator

from users.models import Users

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # content = models.TextField() # For production
    content = models.TextField(null=True, blank=True) # For testing
    urlToImage = models.URLField(max_length=500, null=True, blank=True)
    author_id = models.ForeignKey(Users, related_name='blog_author', on_delete=models.CASCADE)
    visit = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=Posts)