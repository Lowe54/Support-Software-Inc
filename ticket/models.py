import uuid
from django.db import models

from authentication.models import MyUser as Users
# Create your models here.


class Ticket(models.Model):
    '''
    Table to hold core ticket information.
    '''
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MED', 'Medium'),
        ('HGH', 'High'),
    ]
    STATUS_CHOICES = [
        ('OPN', 'Open'),
        ('PEN', 'Pending'),
        ('ONH', 'On Hold'),
        ('CLS', 'Closed'),
    ]
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
        default='NEW'
    )
    raised_on = models.DateTimeField(
        auto_now=True,
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
    )
    priority = models.CharField(
        max_length=3,
        choices=PRIORITY_CHOICES,
        null=False,
        blank=False
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
