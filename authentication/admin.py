'''
Admin.py file for Authentication module
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from django.contrib.auth.models import User

from organisations.models import Organisation

from .models import MyUser


class UserInline(admin.TabularInline):
    '''
    Inline Class for MyUser model
    '''
    model = MyUser


class MyUserAdmin(UA):
    '''
    Defines the Admin class for MyUser

    @inline - UserInline
    '''
    inlines = [
        UserInline
    ]

# Since we are extending the default user, we first need to
# deregister the default User model


admin.site.unregister(User)

# Then re-register them both
admin.site.register(User, MyUserAdmin)
admin.site.register(Organisation)
