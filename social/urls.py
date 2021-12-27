from django.urls import path
from .views import PostModelListView, PostModelDetailView,\
    PostModelUpdateView, PostModelDeleteView, CommentModelDeleteView

app_name = 'social'

urlpatterns = [
    path('', PostModelListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostModelDetailView.as_view(), name='post-detail'),
    path('post/update/<int:pk>/', PostModelUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostModelDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentModelDeleteView.as_view(), name='comment-delete'),
]