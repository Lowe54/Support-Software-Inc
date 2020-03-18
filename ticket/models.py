'''
Model file for ticket(s) table
'''

import uuid

from django.db import models

from authentication.models import MyUser as Users

STATUS_CHOICES = (
    ('OPN', 'Open'),
    ('PEN', 'Pending'),
    ('ONH', 'On Hold'),
    ('CLS', 'Closed'),
)

PRIORITY_CHOICES = (
    ('LOW', 'Low'),
    ('MED', 'Medium'),
    ('HGH', 'High'),
)


class Ticket(models.Model):
    '''
    Table to hold core ticket information.
    '''

    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        null=False,
        blank=False,
        default='OPN'
    )
    raised_on = models.DateTimeField(
        null=False,
        blank=False
    )
    assigned_to = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'AGN'},
        null=True,
        blank=True,
    )
    raised_by = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE,
        related_name='+'
    )
    associated_users = models.ManyToManyField(
        to=Users,
        related_name='+',
        blank=True,
        null=True
    )
    priority = models.CharField(
        max_length=3,
        choices=PRIORITY_CHOICES,
        null=False,
        blank=False,
        default='LOW'
    )
    closed_on = models.DateTimeField(
        blank=True,
        null=True,
    )
    closure_message = models.CharField(
        max_length=150,
        null=True,
        blank=True,

    )
    updated_on = models.DateField(
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        '''
        Return the ticket title
        '''
        return self.title
