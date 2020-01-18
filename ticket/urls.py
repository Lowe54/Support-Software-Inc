'''
Urls.py file for ticket module
'''

from django.urls import path
from .views import dashboard, results
urlpatterns = [
    path(r'dashboard', dashboard, name="dashboard"),
    path(r'results', results, name="results")
]
