'''
Urls.py file for Payment module
'''
from django.urls import path
from .views import render_payment_form, add_order
urlpatterns = [
    path(r'form/', render_payment_form, name="render_payment"),
    path(r'orderconfirmed/', add_order)
]