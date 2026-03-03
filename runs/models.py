from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Extended profile for each user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    middle_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    """A short post (max 42 characters) made by a user."""
    content = models.CharField(max_length=42)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.author.username}: {self.content}'
