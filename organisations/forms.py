from django import forms


class editOrganisationForm(forms.Form):

    id = forms.CharField(
        widget= forms.HiddenInput()
    )
    name = forms.CharField(
        required=True,
        label="Organisation Name"
    )
