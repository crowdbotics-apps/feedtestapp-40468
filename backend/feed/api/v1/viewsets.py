from rest_framework import authentication
from feed.models import Like,Post
from .serializers import LikeSerializer,PostSerializer
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Post.objects.all()

class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Like.objects.all()