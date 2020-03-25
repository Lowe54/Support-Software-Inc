'''
Admin.py file for Payments module
'''
from django.contrib import admin

from .models import Order

admin.site.register(Order)
