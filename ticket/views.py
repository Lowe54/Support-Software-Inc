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
from .forms import FilterForm


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
            unassigned_tickets = len(Ticket.objects.filter(assigned_to=None))
            print(custom_user.user_id)
            assigned_tickets = len(Ticket.objects.filter(
                assigned_to=MyUser.objects.get(user_id=request.user.id)
                ))
            open_tickets = len(Ticket.objects.exclude(
                status='CLS'
            ))
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


@login_required
def results(request):
    '''
    View that returns the results page + filters
    '''
    if request.method == 'GET':
        print(request.GET)
        for key, value in request.GET.items():
            if key == 'status':
                status = Ticket.objects.filter(
                    status=value
                )
            else:
                status = Ticket.objects.none()

            if key == 'statusexclude':
                statusexclude = Ticket.objects.exclude(
                    status=value
                )
            else:
                statusexclude = Ticket.objects.none()

            if key == 'assigned_to':
                if int(value) > 0:
                    assigned_to = Ticket.objects.filter(
                        assigned_to=MyUser.objects.get(user_id=value)
                        )
                else:
                    assigned_to = Ticket.objects.filter(assigned_to=None)

            else:
                assigned_to = Ticket.objects.none()
            ticket_list = status | statusexclude | assigned_to
    else:

        ticket_list = Ticket.objects.all()

    filter_form = FilterForm()
    return render(
        request,
        'results.html',
        {
            'ticket_list': ticket_list,
            'filter_form': filter_form
        }
        )
