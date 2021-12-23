from django import forms
from .models import PostModel

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