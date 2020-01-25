from.models import MyUser

def extended_user(request):
    if hasattr(request, 'user'):
        try:
            user_profile = MyUser.objects.get(user_id=request.user.id)
        except MyUser.DoesNotExist:
            user_profile = None
    return {
        'user_profile': user_profile
    }
