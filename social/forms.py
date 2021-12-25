from django import forms
from .models import PostModel, CommentModel


class PostModelForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Write something'
        })
    )

    class Meta:
        model = PostModel
        fields = ['body']


class CommentModelForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...'
        })
    )

    class Meta:
        model = CommentModel
        fields = ['comment']


