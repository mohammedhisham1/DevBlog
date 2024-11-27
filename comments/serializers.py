from rest_framework import serializers
from .models import Comment
from users.serializers import UserSerializer
from blogs.serializers import BlogSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    blog = BlogSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'blog', 'user', 'content', 'created_at']
