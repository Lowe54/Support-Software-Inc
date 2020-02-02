'''
Urls.py file for ticket module
'''

from django.urls import path
from .views import (dashboard, results, ticket_detail, ticket_assign,
                    edit_ticket, save_ticket)
urlpatterns = [
    path(r'dashboard', dashboard, name="dashboard"),
    path(r'results', results, name="results"),
    path(r'ticket/<uuid:t_id>', ticket_detail, name="ticket_detail"),
    path(r'ticket/assigntouser/', ticket_assign),
    path(r'ticket/edit/', edit_ticket),
    path(r'ticket/save/', save_ticket)
]
