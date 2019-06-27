from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    subscribe = models.BooleanField()
    key = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Article(models.Model):
    name = models.CharField(max_length=50, default='')
    text = models.TextField(default='')
    free = models.BooleanField()
