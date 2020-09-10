from django.db import models
from django.db.models.signals import pre_save
from blog.utils import unique_slug_generator
from django.contrib.auth.models import User


# Create your models here.
class Showcases(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    description = models.TextField()
    author_id = models.ForeignKey(User, related_name='showcase_author', on_delete=models.CASCADE, null=True)
    email = models.EmailField(max_length=254)
    visit = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'showcases'

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Showcases)
