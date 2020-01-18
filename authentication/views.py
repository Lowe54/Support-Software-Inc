'''
Authentication Views

Login
Logout
'''
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import LoginForm


def login(request):
    '''
    Login functionality
    '''
    # If user is already logged in, redirect to index with a page
    if request.user.is_authenticated:
        messages.add_message(
            request,
            messages.INFO,
            "You are already signed in"
            )
        return redirect('/')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user:
                auth.login(user=user, request=request)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "You have successfully logged in"
                    )
                return redirect('/')

            login_form.add_error(
                None,
                "Your username or password is incorrect"
                )
    else:
        login_form = LoginForm()

    return render(request, 'login.html', {'loginForm': login_form})


def logout(request):
    '''
        Signs the user out of the site
    '''
    auth.logout(request)
    messages.add_message(
        request,
        messages.SUCCESS,
        "You have successfully signed out"
        )
    return redirect('/')
