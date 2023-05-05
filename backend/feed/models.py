from django.conf import settings
from django.db import models
from users.models import User

class Post(models.Model):
    'Generated Model'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=2200)
    image = models.ImageField(upload_to='posts/')
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_date']

class Like(models.Model):
    'Generated Model'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post')

class Comment(models.Model):
    'Generated Model'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_date']

# Create your models here.
