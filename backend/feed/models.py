from django.conf import settings
from django.db import models
class Post(models.Model):
    'Generated Model'
    caption = models.CharField(max_length=2200,)
    media = models.CharField(max_length=256,)
    created_date = models.DateTimeField(auto_now_add=True,)
class Like(models.Model):
    'Generated Model'
    created_date = models.DateTimeField(auto_now_add=True,)

# Create your models here.
