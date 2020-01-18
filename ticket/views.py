'''
Views.py file for Ticket Module

dashboard

Ticket_List
Ticket_View

Edit_Ticket
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import MyUser


@login_required
def dashboard(request):
    '''
    View that renders the appropriate dashboard that is visible when
    they sign in
    '''
    if request.user.is_authenticated:
        custom_user = MyUser.objects.get(user_id=request.user.id)
        if custom_user.role != 'AGN':
            return redirect('/')
        return render(request, 'agent_dashboard.html', {'user': custom_user})
    return redirect('login')
