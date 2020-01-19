'''
Forms.py file for Ticket module
'''

from django import forms
from .models import STATUS_CHOICES, PRIORITY_CHOICES


class FilterForm(forms.Form):
    '''
    Form that renders the 'Filters' on the side
    of the results page
    '''
    Keyword = forms.CharField(
        required=False,
        help_text="Enter Keyword to search for"
    )
    status = forms.ChoiceField(
        required=False,
        choices=STATUS_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    priority = forms.ChoiceField(
        required=False,
        choices=PRIORITY_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
