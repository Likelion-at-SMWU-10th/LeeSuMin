from xml.etree.ElementTree import Comment
from django import forms
from .models import Diary, Comment

class DiaryModelForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'body']

class DiaryForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

