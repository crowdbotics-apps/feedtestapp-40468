from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'post')

class Comment(models.Model):
    'Generated Model'
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_date']

# Create your models here.
