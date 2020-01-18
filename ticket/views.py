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
from .models import Ticket


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
        # Try to get a count for each of the 3 counters
        try:
            unassigned_tickets = Ticket.objects.get(assigned_to=None)
            assigned_tickets = Ticket.objects.get(
                assigned_to=custom_user.user_id
                )
            open_tickets = Ticket.objects.get(
                status='OPN'
            )
        # Catch any DoesNotExist errors, which means the count would be 0
        except Ticket.DoesNotExist:
            unassigned_tickets = 0
            assigned_tickets = 0
            open_tickets = 0

        return render(
            request,
            'dashboard.html',
            {
                'user': custom_user,
                'unassigned': unassigned_tickets,
                'assigned': assigned_tickets,
                'open_tickets': open_tickets
            }
        )
    return redirect('login')
