from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    url_key = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='default.png', blank=True)
    # we have 2 tables - users and posts // they both are related -> 1 user can create many posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None) # if user deleted, all posts gets deleted (cascade)

    def __str__(self):
        return self.title
    