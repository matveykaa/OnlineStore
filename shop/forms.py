from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['sender', 'title', 'body']


class ReviewForm(forms.Form):
    review_text = forms.CharField(widget=forms.Textarea)
