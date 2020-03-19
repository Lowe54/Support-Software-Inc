'''
Organisation Model.py file

'''
import uuid

from django.db import models


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
