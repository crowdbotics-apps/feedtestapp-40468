from rest_framework import serializers
from feed.models import Like,Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = "__all__"