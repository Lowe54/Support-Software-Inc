from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def login(request):
    login_form = LoginForm()

    return render(request, 'login.html', {'loginForm' : login_form})