'''
Forms.py file for the authentication app
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(forms.Form):
    '''
    Login Form

    Username - Text field, required
    Password - Password field, required
    '''
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class RegisterForm1(UserCreationForm):
    """ Form used to register a new user """
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        '''
        Function to clean an email
        '''
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        '''
        Function to clean the both passwords and compare
        '''
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError("Please Confirm your password")

        if password1 != password2:
            raise forms.ValidationError("Passwords must match")

        return password2


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']
