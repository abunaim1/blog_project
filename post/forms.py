from django import forms
from post.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        # fields = '__all__'
        