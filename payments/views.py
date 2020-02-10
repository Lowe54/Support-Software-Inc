'''
Views.py file for Payments app
'''
import os
import logging
from datetime import date
from django.shortcuts import render, HttpResponse
import stripe
from authentication.models import MyUser
from .models import Order
from .forms import OrderForm


def render_payment_form(request):

    stripe.api_key = os.getenv('STRIPE_SECRET')

    intent = stripe.PaymentIntent.create(
        amount=30,
        currency='gbp',
    )

    order_form = OrderForm()

    return render(
        request,
        'payment_form.html',
        {
            'cs': intent.client_secret,
            'o_form': order_form
        }
    )


def add_order(request):
    logger = logging.getLogger(__name__)
    logger.info('Add Order Called, checking request method')
    if request.method == 'POST':
        logger.info('Method is Post, now checking for logged in user')
        if request.user:
            Order.objects.create(
                user=MyUser.objects.get(user_id=request.user.id),
                full_name=request.POST['full_name'],
                street_address1=request.POST['street_address_1'],
                street_address2=request.POST['street_address_2'],
                town_or_city=request.POST['town_or_city'],
                county=request.POST['county'],
                country=request.POST['country'],
                phone_number=request.POST['phone_number'],
                date=date.today(),
                amount=request.POST['amount'],
                confirmation_code=request.POST['confirmation_code']
            )
        else:
            Order.objects.create(
                full_name=request.POST['full_name'],
                street_address1=request.POST['street_address_1'],
                street_address2=request.POST['street_address_2'],
                town_or_city=request.POST['town_or_city'],
                county=request.POST['county'],
                country=request.POST['country'],
                phone_number=request.POST['phone_number'],
                date=date.today(),
                amount=request.POST['amount'],
                confirmation_code=request.POST['confirmation_code']
            )
        return HttpResponse(status=200)
    return HttpResponse(status=403)
