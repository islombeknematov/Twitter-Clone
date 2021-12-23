from django.urls import path
from .views import PostModelListView
app_name = 'social'

urlpatterns = [
    path('', PostModelListView.as_view(), name='post-list'),
]