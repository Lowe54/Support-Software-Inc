'''
Forms.py file for Organisation

Organisation Form - Used to Add / Edit Organisations
Un-associated User Form - Shows all unassociated users

'''
from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm

from authentication.models import MyUser

from .models import Organisation


class OrganisationForm(ModelForm):
    '''
    Form that allows addition or editing
    of an organisation
    '''
    class Meta:
        model = Organisation
        fields = ['Organisation_Name']


class UnassociatedUserForm(forms.Form):
    '''
    Form that shows all users
    not associated with an
    organisation
    '''
    def __init__(self, *args, **kwargs):
        super(UnassociatedUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'custom-control custom-checkbox'

        self.fields['users'] = forms.MultipleChoiceField(
            choices=[(o.user_id, o.get_username_and_email())
                     for o in MyUser.objects.filter(organisation_id=None)],
            widget=forms.CheckboxSelectMultiple
        )
