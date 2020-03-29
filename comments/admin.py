'''
Comments module admin file
'''
from django.contrib import admin
from .models import Comment

admin.site.register(Comment)
