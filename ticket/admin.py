'''
Admin.py file for Ticket Module
'''
from django.contrib import admin

from .models import Ticket


class TicketAdmin(admin.ModelAdmin):
    '''
    Ticket Admin class

    Will display the ID, Title, Raised On date and Status
    '''
    list_display = ('id', 'title', 'raised_on', 'status')

admin.site.register(Ticket, TicketAdmin)
