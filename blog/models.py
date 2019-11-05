from django.db import models
from django.conf import settings
from django.utils import timezone


class PostManager(models.Manager):
    def createPost(self, author, title, text, date):
        post = self.create(author,title,text,date)
        return post


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    objects = PostManager()

    def __str__(self):
        return self.title
