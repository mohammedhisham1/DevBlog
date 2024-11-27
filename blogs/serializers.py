from rest_framework import serializers
from .models import Blog
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'content', 'author', 'category',
            'created_at', 'updated_at'
        ]
