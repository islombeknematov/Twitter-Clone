from django.contrib import admin
from .models import PostModel

# admin.site.register(PostModel)
@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at']

