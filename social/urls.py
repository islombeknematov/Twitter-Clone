from django.urls import path
from .views import PostModelListView, PostModelDetailView, \
    PostModelUpdateView, PostModelDeleteView, CommentModelDeleteView, UserProfileModelView, ProfileModelUpdateView, \
    AddFollower, RemoveFollower, PostAddLike, PostAddDislike, UserSearch, ListFollowers, CommentAddLike, \
    CommentAddDislike, CommentReplyView, PostNotification, FollowNotification, RemoveNotification, CreateThread, \
    ListThreads, ThreadView, CreateMessage

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

    path('post/<int:pk>/like/', PostAddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike/', PostAddDislike.as_view(), name='dislike'),

    path('post/<int:post>/comment/<int:pk>/like/', CommentAddLike.as_view(), name='comment-like'),
    path('post/<int:post>/comment/<int:pk>/dislike/', CommentAddDislike.as_view(), name='comment-dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/reply/', CommentReplyView.as_view(), name='comment-reply'),

    path('search/', UserSearch.as_view(), name='profile-search'),

    path('profile/<int:pk>/followers/', ListFollowers.as_view(), name='list-followers'),

    path('notification/<int:notification_pk>/post/<int:post_pk>/', PostNotification.as_view(),
         name='post-notification'),
    path('notification/<int:notification_pk>/profile/<int:profile_pk>/', FollowNotification.as_view(),
         name='follow-notification'),

    path('notification/delete/<int:notification_pk>/', RemoveNotification.as_view(), name='notification-delete'),

    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create-thread/', CreateThread.as_view(), name='create-thread'),

    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),


]
