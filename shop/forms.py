from django import forms


class ReviewForm(forms.Form):
    review_text = forms.CharField(widget=forms.Textarea)
