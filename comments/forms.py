from django import forms
from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):

    comment_content = forms.CharField(
        label="Content",
        widget=forms.Textarea()
    )
    is_request_update = forms.BooleanField()

    class Meta:
        model = Comment
        fields = ['comment_content', 'posted_by', 'is_internal_comment']
