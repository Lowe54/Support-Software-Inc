from django import forms

class LoginForm(forms.Form):
    '''
    Login Form

    Username - Text field, required
    Password - Password field, required
    '''
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
