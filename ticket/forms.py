'''
Forms.py file for Ticket module
'''
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
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
        self.helper.form_method = 'GET'
        self.helper.form_class = 'custom-control custom-checkbox'
        self.helper.add_input(Submit('submit', 'Submit'))

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


class AgentTicketForm(ModelForm):
    '''
    Define the fields that an agent can update
    when editing a ticket
    '''
    class Meta:
        model = Ticket
        fields = (['title', 'description', 'status',
                   'priority', 'associated_users'])


class UserTicketForm(ModelForm):
    '''
    Define the fields that an end user can update
    when editing a ticket
    '''
    class Meta:
        model = Ticket
        fields = (['title', 'description'])


class AddTicketForm(ModelForm):
    '''
    Define the fields present in the 'add ticket' form
    '''
    class Meta:
        model = Ticket
        fields = (['title', 'description', 'priority'])
