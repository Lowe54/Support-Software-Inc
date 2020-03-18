'''
Views.py file for authentication app

'''
import csv

import sweetify
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import HttpResponse, redirect, render, reverse

from .forms import LoginForm, ProfileForm, RegisterForm1
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


def get_profile_edit_form(request):
    '''
    Returns a form instance allowing the user to edit their profile
    '''
    profile_id = request.POST['profile_id']
    if profile_id is not None:
        user = User.objects.get(id=profile_id)
        profile_form = ProfileForm(instance=user)
        return render(
                        request,
                        'profile_form.html',
                        {
                            'profile_form': profile_form
                        }
                     )


def save_profile(request):
    '''
    Save the users profile (Core details)
    '''

    if request.method == 'POST':
        profile_id = request.POST['user_id']
        user = User.objects.get(id=profile_id)
        profile = ProfileForm(request.POST, instance=user)
        profile_completed = profile.save()
        response = '<dl class="no-bullet row">\
                        <dt class="col-sm-3">Username :</dt>\
                        <dd class="col-sm-9">{}</dd>\
                        <dt class="col-sm-3">Email :</dt>\
                        <dd class="col-sm-9">{}</dd>\
                        <dt class="col-sm-3">First Name :</dt>\
                        <dd class="col-sm-9">{}</dd>\
                        <dt class="col-sm-3">Last Name :</dt>\
                        <dd class="col-sm-9">{}</dd>\
                    </dl>'.format(profile_completed.username,
                                  profile_completed.email,
                                  profile_completed.first_name,
                                  profile_completed.last_name)
        return HttpResponse(status=200, content=response)

    return HttpResponse(status=403)


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


@login_required
def import_user_data(request):
    with open('MOCK_DATA.csv', 'r') as csvfile:
        user_import = csv.DictReader(csvfile)
        for new_user in user_import:
            user = User.objects.create_user(
                username=new_user['username'],
                email=new_user['email'],
                password=new_user['password']
            )
            user.save()
            MyUser.objects.create(
                user=User.objects.get(id=user.id),
                role='USR',
            )
