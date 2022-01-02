from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class PostModel(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    like = models.ManyToManyField(User, blank=True, related_name='like')
    dislike = models.ManyToManyField(User, blank=True, related_name='dislike')

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


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user',
                                related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='profile_photos',
                                default='profile_photos/default_image.png', null=True, blank=True)

    followers = models.ManyToManyField(User, blank=True, related_name='followers')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'users profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileModel.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()








