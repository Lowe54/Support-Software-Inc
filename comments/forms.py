from django import forms
from django.forms import ModelForm

from .models import Comment


class CommentForm(ModelForm):

    comment_content = forms.CharField(
        label="Content",
        widget=forms.Textarea()
    )
    is_internal_comment = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'data-toggle': 'toggle',
                'data-on': 'Yes',
                'data-off': 'No',
                'data-onstyle': 'success',
                'data-offstyle': 'danger',
            }
        )
    )

    class Meta:
        model = Comment
        fields = ['comment_content', 'is_internal_comment']
