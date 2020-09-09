from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    about_me = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name
