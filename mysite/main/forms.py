from django import forms
from .models import Post, Check


class PostForm(forms.ModelForm):
    class Meta(object):
        model = Post
        fields = ('title',)


class Checkbox(forms.ModelForm):

    class Meta(object):
        model = Check
        fields = ('phonetic', 'harmony', 'syllableH', 'syllableM', 'syllableCount')
