'''
Urls.py file for ticket module
'''

from django.urls import path
from .views import dashboard
urlpatterns = [
    path(r'/dashboard', dashboard, name="dashboard")
]
