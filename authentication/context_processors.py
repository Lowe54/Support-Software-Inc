'''
Custom context processors to add MyUser Fields to the context
'''
from.models import MyUser

def extended_user(request):
    '''
    Extended User

    @var user_profile - Context to hold the MyUser details for the logged in
    profile
    '''
    if hasattr(request, 'user'):
        try:
            user_profile = MyUser.objects.get(user_id=request.user.id)
        except MyUser.DoesNotExist:
            user_profile = None
    return {
        'user_profile': user_profile
    }
