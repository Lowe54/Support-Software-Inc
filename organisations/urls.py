from django.urls import path

from .views import (show_organisation_list, add_or_edit_organisation,
                    get_user_list)

urlpatterns = [
    path(r'list', show_organisation_list, name="show_organisation_list"),
    path(r'edit/', add_or_edit_organisation, name="edit_organisation"),
    path(r'userlist/', get_user_list, name="get_organisation_users"),
]