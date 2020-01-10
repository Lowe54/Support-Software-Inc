from django.urls import path
from .views import login
urlpatterns = [
    path(r'login', login, name="login")
]
