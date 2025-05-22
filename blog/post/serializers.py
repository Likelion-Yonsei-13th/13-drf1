from rest_framework import serializers
from .models import Post

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user']
        # fields = ['id', 'title', 'content', 'created_at', 'user']
        read_only_fields = ['user']