from crispy_forms.helper import FormHelper
from django import forms
from django.forms import ModelForm

from authentication.models import MyUser

from .models import Organisation


class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        fields = ['Organisation_Name']


class UnassociatedUserForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(UnassociatedUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'custom-control custom-checkbox'

        self.fields['users'] = forms.MultipleChoiceField(
            choices=[(o.user_id, o.get_username_and_email())
                     for o in MyUser.objects.filter(organisation_id=None)],
            widget=forms.CheckboxSelectMultiple
        )
