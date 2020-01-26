'''
Authentication Views

Login
Logout
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
import sweetify
from .forms import LoginForm
from .models import MyUser


def login(request):
    '''
    Login functionality
    '''
    # If user is already logged in, redirect to index
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
                sweetify.success(
                    request,
                    "You have successfully signed in",
                    button='Ok',
                    timer=5000
                )
                return redirect('dashboard')

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
    sweetify.success(
        request,
        "You have successfully signed out",
        button='Ok',
        timer=5000
    )
    return redirect('/')


@login_required
def profile_view(request):
    '''
    Shows the logged in user their profile
    '''
    user = MyUser.objects.get(user_id=request.user.id)
    print(user.user.email)
    return render(request, 'profile_view.html', {'user': user})
