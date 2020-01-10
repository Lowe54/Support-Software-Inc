import uuid
from django.db import models
from django.contrib.auth.models import User

class Organisation(models.Model):
    '''
    Organisation Table

    id - Organisations ID
    name - Organisations Name (Max length of 255 characters)
    '''
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
        )
    Organisation_Name = models.CharField(
        max_length=255,
        name="Organisation_Name"
        )
    def __str__(self):
        '''
        Returns the Organisation's Name
        '''
        return self.Organisation_Name

class MyUser(models.Model):
    '''
    User Table - Extends the base User model via Abstract User
    profile_picture - Image Field that holds the user's profile image
    organisation - One to Many relationship - Organisation table id
    '''
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    profile_picture = models.ImageField(
        name="Profile Picture",
        upload_to='',
        null=True,
        blank=True
        )
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )