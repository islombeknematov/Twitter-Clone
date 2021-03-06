from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import PostModelForm, CommentModelForm, ThreadForm, MessageForm
from .models import PostModel, CommentModel, UserProfileModel, NotificationModel, ThreadModel, MessageModel
from django.views.generic.edit import UpdateView, DeleteView


class PostModelListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logged_in_user = request.user
        posts = PostModel.objects.filter(
            author__profile__followers__in=[logged_in_user.id]
        ).order_by('-created_at')
        form = PostModelForm()
        context = {
            'post_list': posts,
            'form': form,

        }
        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        logged_in_user = request.user
        posts = PostModel.objects.filter(
            author__profile__followers__in=[logged_in_user.id]
        ).order_by('-created_at')
        form = PostModelForm(request.POST, files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,

        }
        return render(request, 'social/post_list.html', context)


class PostModelDetailView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        post = PostModel.objects.get(pk=pk)
        form = CommentModelForm()
        comments = CommentModel.objects.filter(post=post).order_by('-created_at')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = PostModel.objects.get(pk=pk)
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = CommentModel.objects.filter(post=post).order_by('-created_at')

        notification = NotificationModel.objects.create(
            notification_type=2, from_user=request.user,
            to_user=post.author, post=post
        )

        context = {
            'post': post,
            'form': form,
            'comments': comments,

        }

        return render(request, 'social/post_detail.html', context)


class PostModelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostModel
    fields = ['body']
    template_name = 'social/post_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostModelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostModel
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('social:post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CommentModelDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CommentModel
    template_name = 'social/comment_delete.html'

    # success_url = reverse_lazy('social:post-detail')

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('social:post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class UserProfileModelView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfileModel.objects.get(pk=pk)
        user = profile.user
        posts = PostModel.objects.filter(author=user).order_by('-created_at')

        # Start adding followers
        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)
        # End adding followers

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
        }

        return render(request, 'social/profile.html', context)


class ProfileModelUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfileModel
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'social/profile_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('social:user-profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfileModel.objects.get(pk=pk)
        profile.followers.add(request.user)

        notification = NotificationModel.objects.create(
            notification_type=3, from_user=request.user,
            to_user=profile.user
        )

        return redirect('social:user-profile', pk=profile.pk)


class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfileModel.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('social:user-profile', pk=profile.pk)


class PostAddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = PostModel.objects.get(pk=pk)

        is_dislike = False
        for dislike in post.dislike.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislike.remove(request.user)

        is_like = False
        for like in post.like.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.like.add(request.user)
            notification = NotificationModel.objects.create(
                notification_type=3, from_user=request.user,
                to_user=post.author, post=post
            )

        if is_like:
            post.like.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class PostAddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = PostModel.objects.get(pk=pk)

        is_like = False
        for like in post.like.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.like.remove(request.user)

        is_dislike = False
        for dislike in post.dislike.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislike.add(request.user)

        if is_dislike:
            post.dislike.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = UserProfileModel.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }
        return render(request, 'social/search.html', context)


class ListFollowers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfileModel.objects.get(pk=pk)
        followers = profile.followers.all()

        context = {
            'profile': profile,
            'followers': followers
        }
        return render(request, 'social/followers_list.html', context)


class CommentAddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = CommentModel.objects.get(pk=pk)

        is_dislike = False
        for dislike in comment.dislike.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislike.remove(request.user)

        is_like = False
        for like in comment.like.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            comment.like.add(request.user)
            notification = NotificationModel.objects.create(
                notification_type=1, from_user=request.user,
                to_user=comment.author, comment=comment
            )

        if is_like:
            comment.like.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class CommentAddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = CommentModel.objects.get(pk=pk)

        is_like = False
        for like in comment.like.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.like.remove(request.user)

        is_dislike = False
        for dislike in comment.dislike.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislike.add(request.user)

        if is_dislike:
            comment.dislike.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class CommentReplyView(LoginRequiredMixin, View):
    def post(self, request, post_pk, pk, *args, **kwargs):
        post = PostModel.objects.get(pk=post_pk)
        parent_comment = CommentModel.objects.get(pk=pk)
        form = CommentModelForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            new_comment.save()

        notification = NotificationModel.objects.create(
            notification_type=2, from_user=request.user,
            to_user=parent_comment.author, comment=new_comment
        )

        return redirect('social:post-detail', pk=post.pk)


class PostNotification(View):

    def get(self, request, notification_pk, post_pk, *args, **kwargs):
        notification = NotificationModel.objects.get(pk=notification_pk)
        post = PostModel.objects.get(pk=post_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('social:post-detail', pk=post_pk)


class FollowNotification(View):

    def get(self, request, notification_pk, profile_pk, *args, **kwargs):
        notification = NotificationModel.objects.get(pk=notification_pk)
        profile = UserProfileModel.objects.get(pk=profile_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('social:user-profile', pk=profile_pk)


class RemoveNotification(View):
    def delete(self, request, notification_pk, *args, **kwargs):
        notification = NotificationModel.objects.get(pk=notification_pk)

        notification.user_has_seen = True
        notification.save()

        return HttpResponse("Success", content_type='text/plain')


class ListThreads(View):

    def get(self, request, *args, **kwargs):
        threads = ThreadModel.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads': threads
        }
        return render(request, 'social/inbox.html', context)


class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()
        context = {
            'form': form
        }
        return render(request, 'social/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)
        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if ThreadModel.objects.filter(user=request.user, receiver=receiver).exists():
                thread = ThreadModel.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('social:thread', pk=thread.pk)

            elif ThreadModel.objects.filter(user=receiver, receiver=request.user).exists():
                thread = ThreadModel.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('social:thread', pk=thread.pk)

            if form.is_valid():
                thread = ThreadModel(user=request.user, receiver=receiver)
                thread.save()
                return redirect('social:thread', pk=thread.pk)

        except:
            return redirect('social:create-thread')


class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = ThreadModel.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)

        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list,
        }
        return render(request, 'social/thread.html', context)


class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        thread = ThreadModel.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(
            thread=thread,
            sender_user=request.user,
            receiver_user=receiver,
            body=request.POST.get('message')
        )

        message.save()
        return redirect('social:thread', pk=pk)






