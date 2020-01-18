'''
Admin.py file for Ticket Module
'''
from django.contrib import admin
from .models import Ticket


admin.site.register(Ticket)
