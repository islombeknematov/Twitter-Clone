from django.shortcuts import render
from .forms import PostModelForm
from django.views import View
from .models import PostModel


class PostModelListView(View):

    def get(self, request, *args, **kwargs):
        posts = PostModel.objects.all().order_by('-created_at')
        form = PostModelForm()
        context = {
            'post_list': posts,
            'form': form,

        }
        return render(request, 'social/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = PostModel.objects.all().order_by('-created_at')
        form = PostModelForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,

        }
        return render(request, 'social/post_list.html', context)
