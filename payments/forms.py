'''
Forms.py file for Payment module
'''
from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    '''
    Standard Order form
    '''
    class Meta:
        model = Order
        fields = ('full_name', 'street_address1',
                  'street_address2', 'county', 'country', 'town_or_city',
                  'phone_number')
