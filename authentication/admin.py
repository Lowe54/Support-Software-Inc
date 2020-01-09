from django.contrib import admin
from .models import MyUser, Organisation
from django.contrib.auth.models import User

from .models import MyUser
# Register your models here.
class User_Inline(admin.TabularInline):
    model = MyUser

class UserAdmin(admin.ModelAdmin):
    inlines = [
        User_Inline
    ]

# Since we are extending the default user, we first need to
# deregister the default User model
admin.site.unregister(User)

# Then re-register them both
admin.site.register(User, UserAdmin)
admin.site.register(Organisation)