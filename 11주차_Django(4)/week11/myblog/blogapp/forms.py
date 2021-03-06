from django import forms
from .models import Blog,Comment

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        