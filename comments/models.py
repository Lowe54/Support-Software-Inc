import uuid

from django.db import models

from authentication.models import MyUser
from ticket.models import Ticket


class Comment(models.Model):
    comment_id = models.UUIDField(
        'Issue ID',
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    comment_content = models.TextField()

    posted_by = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    date_posted = models.DateTimeField(
        'Posted On',
        auto_now=True,
        null=False,
        blank=False
    )

    is_internal_comment = models.NullBooleanField(
        default=False,
        null=True,
        blank=True
    )

    related_ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.comment_content
