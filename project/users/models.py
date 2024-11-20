from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_user_permissions'  # Добавляем related_name здесь
    )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_groups'  # Добавляем related_name здесь
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'




class Link(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    link_type = models.CharField(max_length=50, choices=(('website', 'Website'), ('book', 'Book'), ('article', 'Article'), ('music', 'Music'), ('video', 'Video')), default='website')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return self.title or self.url
