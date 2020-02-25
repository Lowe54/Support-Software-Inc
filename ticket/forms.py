'''
Forms.py file for Ticket module
'''
from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm

from .models import PRIORITY_CHOICES, STATUS_CHOICES, Ticket


class FilterForm(forms.Form):
    '''
    Form that renders the 'Filters' on the side
    of the results page
    '''
    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'custom-control custom-checkbox'
        
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


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = (['title', 'description', 'status',
                   'priority', 'associated_users'])


class AddTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = (['title', 'description', 'priority'])
