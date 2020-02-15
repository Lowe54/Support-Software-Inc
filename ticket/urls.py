'''
Urls.py file for ticket module
'''

from django.urls import path

from .views import (close_ticket, dashboard, edit_ticket, results, save_ticket,
                    ticket_assign, ticket_detail)

urlpatterns = [
    path(r'dashboard', dashboard, name="dashboard"),
    path(r'results', results, name="results"),
    path(r'ticket/<uuid:t_id>', ticket_detail, name="ticket_detail"),
    path(r'ticket/assigntouser/', ticket_assign),
    path(r'ticket/edit/', edit_ticket),
    path(r'ticket/save/', save_ticket),
    path(r'ticket/close/', close_ticket),
]
