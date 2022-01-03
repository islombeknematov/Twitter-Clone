from django.urls import path
from .views import PostModelListView, PostModelDetailView, \
    PostModelUpdateView, PostModelDeleteView, CommentModelDeleteView, UserProfileModelView, ProfileModelUpdateView, \
    AddFollower, RemoveFollower, AddLike, AddDislike, UserSearch

app_name = 'social'

urlpatterns = [
    path('', PostModelListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostModelDetailView.as_view(), name='post-detail'),
    path('post/update/<int:pk>/', PostModelUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostModelDeleteView.as_view(), name='post-delete'),

    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentModelDeleteView.as_view(), name='comment-delete'),

    path('profile/<int:pk>/', UserProfileModelView.as_view(), name='user-profile'),
    path('profile/update/<int:pk>/', ProfileModelUpdateView.as_view(), name='update-profile'),

    path('profile/<int:pk>/followers/add/', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove/', RemoveFollower.as_view(), name='remove-follower'),

    path('post/<int:pk>/like/', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike/', AddDislike.as_view(), name='dislike'),

    path('search/', UserSearch.as_view(), name='profile-search')

]