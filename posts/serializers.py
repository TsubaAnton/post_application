from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'image', 'author', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

