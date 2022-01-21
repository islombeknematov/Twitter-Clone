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
    image = forms.ImageField(required=False)

    class Meta:
        model = PostModel
        fields = ['body', 'image']


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


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)






