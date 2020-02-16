from django.shortcuts import render, HttpResponse
from authentication.models import MyUser

from Ticket.models import Ticket
from .models import Comment


def comment(request):
    if request.method == 'POST':
        return HttpResponse(status=200)
    return HttpResponse(status=403)