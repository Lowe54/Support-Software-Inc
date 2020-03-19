'''
Views.py file for authentication app

'''
import sweetify
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import (HttpResponse, get_object_or_404, redirect,
                              render, reverse)

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
                    icon='success',
                    timer='5000',
                    button='Ok',
                    toast='true',
                    position='top-end',
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
        icon='success',
        timer='5000',
        button='Ok',
        toast='true',
        position='top-end',
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
    return HttpResponse(status=401)

def save_profile(request):
    '''
    Save the users profile (Core details)
    '''

    if request.method == 'POST':
        profile_id = request.POST['user_id']
        user = get_object_or_404(User, id=profile_id)
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
                    icon='success',
                    timer='5000',
                    button='Ok',
                    toast='true',
                    position='top-end',
                )
                return redirect(reverse('dashboard'))

            sweetify.error(
                request,
                "Unable to register at this time",
                icon='error',
                timer='5000',
                button='Ok',
                toast='true',
                position='top-end',
            )
    else:
        registration_form = RegisterForm1()
    return render(request, 'register.html', {
        "registration_form": registration_form})
