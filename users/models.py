from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('blogger', 'Blogger'),
        ('reader', 'Reader'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='reader')

    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
