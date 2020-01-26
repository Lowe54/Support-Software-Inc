from django.urls import path

from .views import show_organisation_list

urlpatterns = [
    path(r'list', show_organisation_list, name="show_organisation_list")
]