from django.forms import ModelForm
from .models import Organisation


class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        fields = ['Organisation_Name']
