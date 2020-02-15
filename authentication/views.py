'''
Views.py file for authentication app

'''
import sweetify
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse

from .forms import LoginForm, RegisterForm1
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


def register(request):

    """ Render the registration page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = RegisterForm1(request.POST)

        if registration_form.is_valid():
            user = registration_form.save()
            MyUser.objects.create(
                user=User.objects.get(pk=user.id),
                role='USR',

            )

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                sweetify.success(
                    request,
                    "You have successfully registered",
                    button='Ok',
                    timer=5000
                )
                return redirect(reverse('dashboard'))
            else:
                sweetify.error(
                    request,
                    "Unable to register at this time",
                    button='Ok',
                    timer=5000
                )
    else:
        registration_form = RegisterForm1()
    return render(request, 'register.html', {
        "registration_form": registration_form})
