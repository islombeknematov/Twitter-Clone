from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User


class PostModel(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.author or None

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class CommentModel(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
