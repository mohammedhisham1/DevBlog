from django.db import models
from users.models import User
from categories.models import Category

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
