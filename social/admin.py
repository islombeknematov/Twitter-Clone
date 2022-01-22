from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import PostModel, UserProfileModel, CommentModel, NotificationModel


# admin.site.register(PostModel)
@admin.register(PostModel)
class PostModelAdmin(TranslationAdmin):
    list_display = ['author', 'created_at']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


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
