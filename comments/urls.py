from django.conf.urls import url
from .views import comment

urlpatterns = [
    url(r'comment/post', comment, name="comment")
]
