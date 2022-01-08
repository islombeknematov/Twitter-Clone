from django.contrib import admin
from .models import PostModel, UserProfileModel, CommentModel, NotificationModel


# admin.site.register(PostModel)
@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at']


# admin.site.register(UserProfileModel)
@admin.register(UserProfileModel)
class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'created_at']


# admin.site.register(CommentModel)
@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at']


admin.site.register(NotificationModel)
# @admin.register(NotificationModel)
# class NotificationModelAdmin(admin.ModelAdmin):
    # list_display =



