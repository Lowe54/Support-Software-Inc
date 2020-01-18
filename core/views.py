'''
Views.py page for Core module

Index
'''
from django.shortcuts import render


def index(request):
    """
    Function that returns the index page
    """
    return render(request, 'index.html')
