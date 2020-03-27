'''
Comments module forms.py file
'''
from django import forms
from django.forms import ModelForm

from .models import Comment


class AgentCommentForm(ModelForm):
    '''
    Define the agent's version of the comment form
    '''

    comment_content = forms.CharField(
        label="Content",
        widget=forms.Textarea()
    )

    is_internal_comment = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'data-toggle': 'toggle',
                'data-size': 'md',
                'data-onstyle': 'success',
                'data-offstyle': 'danger',
                'data-on': 'Yes',
                'data-off': 'No',
            }
        )
    )

    class Meta:
        model = Comment
        fields = ['comment_content', 'is_internal_comment']


class UserCommentForm(ModelForm):
    '''
    Define the end user comment form
    '''
    comment_content = forms.CharField(
        label="Content",
        widget=forms.Textarea()
    )
    class Meta:
        model = Comment
        fields = ['comment_content']
