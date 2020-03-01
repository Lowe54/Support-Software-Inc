'''
Views.py file for Ticket Module

dashboard

Ticket_List
Ticket_View

Edit_Ticket
'''
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect, render

from authentication.models import MyUser
from comments.models import Comment

from .forms import AddTicketForm, FilterForm, TicketForm
from .models import Ticket


@login_required
def dashboard(request):
    '''
    View that renders the appropriate dashboard that is visible when
    they sign in
    '''
    if request.user.is_authenticated:
        try:
            custom_user = MyUser.objects.get(user_id=request.user.id)
        except MyUser.DoesNotExist:
            return redirect('index')

        if custom_user.role != 'AGN':
            try:
                my_open_tickets = len(
                    Ticket.objects.filter(
                        status='OPN',
                        raised_by=custom_user))

                tickets_awaiting_feedback = len(Ticket.objects.filter(
                    raised_by=custom_user, status='PEN'
                ))
            except Ticket.DoesNotExist:
                my_open_tickets = 0
                tickets_awaiting_feedback = 0

            return render(
                request,
                'dashboard.html',
                {
                    'user': custom_user,
                    'open_tickets': my_open_tickets,
                    'tickets_feedback': tickets_awaiting_feedback
                }
            )

        else:
            # Try to get a count for each of the 3 counters
            try:
                unassigned_tickets = len(Ticket.objects.filter(
                    assigned_to=None))
                assigned_tickets = len(Ticket.objects.filter(
                    assigned_to=MyUser.objects.get(user_id=request.user.id)
                    ).exclude(status='CLS'))
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
    try:
        custom_user = MyUser.objects.get(user_id=request.user.id)
    except MyUser.DoesNotExist:
        return redirect('index')

    if request.method == 'GET':
        ticket_list = Ticket.objects.all()
        if custom_user.role == 'USR':
            user_id = Ticket.objects.filter(raised_by=custom_user)
            ticket_list = ticket_list & user_id
        for key, value in request.GET.items():
            if key == 'Keyword':
                keyword = Ticket.objects.filter(
                    title__contains=value
                )
                ticket_list = ticket_list & keyword

            if key == 'priority':
                if len(request.GET.getlist(key)) > 1:
                    priority = Ticket.objects.none()
                    value = request.GET.getlist(key)
                    for val in value:
                        pri = Ticket.objects.filter(
                            priority=val
                        )
                        priority = priority | pri
                else:
                    priority = Ticket.objects.filter(
                        priority=value
                    )
                ticket_list = ticket_list & priority

            if key == 'status':
                status = Ticket.objects.filter(
                    status=value
                )
                ticket_list = ticket_list & status

            if key == 'statusexclude':
                statusexclude = Ticket.objects.exclude(
                    status=value
                )
                ticket_list = ticket_list & statusexclude

            if key == 'assigned_to':
                if int(value) > 0:
                    assigned_to = Ticket.objects.filter(
                        assigned_to=MyUser.objects.get(user_id=value)
                        )
                else:
                    assigned_to = Ticket.objects.filter(assigned_to=None)
                ticket_list = ticket_list & assigned_to

            if key == 'raised_by':
                if int(value) > 0:
                    raised_by = Ticket.objects.filter(
                        raised_by=MyUser.objects.get(user_id=value)
                        )
                ticket_list = ticket_list & raised_by
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


@login_required
def ticket_detail(request, t_id):
    ticket = Ticket.objects.get(id=t_id)
    user_profile = MyUser.objects.get(user_id=request.user.id)
    if user_profile.role == 'USR':
        related_comments = Comment.objects.filter(
            related_ticket=t_id
        ).exclude(is_internal_comment=True)
    else:
        related_comments = Comment.objects.filter(related_ticket=t_id)
    return render(
        request,
        'ticket.html',
        {
            'ticket': ticket,
            'relatedcomments': related_comments
        }
    )


def ticket_assign(request, t_id=None):
    if request.method == 'POST':
        user = MyUser.objects.get(user_id=request.POST['assignee'])
        if user:
            ticket = Ticket.objects.get(id=request.POST['t_id'])
            if ticket:
                ticket.assigned_to = user
                ticket.save()
                response = user.user.username
                return HttpResponse(response, status=200)
            return HttpResponse("Error assigning user", status=400)
        return HttpResponse("Error assigning user", status=400)

    return HttpResponse('', status=400)


def edit_ticket(request, t_id=None):
    '''
    Returns the modal containing editable core ticket information
    '''
    if request.method == 'POST':
        if request.POST:
            ticket = Ticket.objects.get(id=request.POST['t_id'])
            if ticket:
                form = TicketForm(instance=ticket)
                return render(
                    request,
                    'edit_ticket_details.html',
                    {'ticket': ticket, 'form': form}
                )

    return HttpResponse(status=400, reason="Bad ticket ID or ticket not found")


def save_ticket(request, t_id=None):
    if request.method == 'POST':
        ticket = Ticket.objects.get(id=request.POST['t_id'])
        if ticket:
            ticket_to_save = TicketForm(request.POST, instance=ticket)
            ticket_data = ticket_to_save.save()
            data = {
                'title': ticket_data.title,
                'description': ticket_data.description,
                'status': ticket_data.get_status_display(),
                'priority': ticket_data.get_priority_display(),
            }
            return JsonResponse(data)


def close_ticket(request, t_id=None):
    if request.method == 'POST':
        ticket = Ticket.objects.get(id=request.POST['t_id'])
        if ticket:
            now = datetime.now()
            ticket.closure_message = request.POST['closure_message']
            ticket.closed_on = now
            ticket.status = 'CLS'
            ticket.save()

            response = "Ticket closed at {} with the following\
                reason '{}'".format(
                    now.strftime("%d/%m/%Y %H:%M:%S"),
                    request.POST['closure_message']
                )
            return HttpResponse(response, status=200)
    return HttpResponse('Unauthorised', status=403)


@login_required
def add_ticket(request):
    if request.method == 'POST':
        ticket_form = AddTicketForm(request.POST)
        if ticket_form.is_valid():
            ticket = Ticket(
                title=request.POST['title'],
                description=request.POST['description'],
                priority=request.POST['priority'],
                raised_by=MyUser.objects.get(user_id=request.user.id)
            )
            ticket.save()
            return redirect('dashboard')
    else:
        ticket_form = AddTicketForm()

    return render(request, 'add_ticket.html', {'form': ticket_form})
