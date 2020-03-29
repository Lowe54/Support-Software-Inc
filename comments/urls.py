'''
Comment module URL file
'''
from django.conf.urls import url

from .views import comment, comment_form

urlpatterns = [
    url(r'new/', comment_form),
    url(r'post/', comment, name="comment")
]
