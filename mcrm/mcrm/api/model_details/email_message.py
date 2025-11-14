from django.db import models

from .email import Email

class EmailMessage(models.Model):
    
    sender = models.CharField(
        max_length = 100
    )
    recipient = models.CharField(
        max_length = 100
    )
    cc = models.JSONField(
        blank = True, null = True
    )
    subject = models.CharField(
        max_length = 255
    )
    body = models.TextField(
        blank = True, null = True
    )
    date_sent = models.DateTimeField(blank = True, null = True)
    date_received = models.DateTimeField(blank = True, null = True)
    is_read = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    attachments = models.JSONField(
        blank = True, null = True
    )
    is_draft = models.BooleanField(default=False)
    email = models.ForeignKey(
        Email,
        on_delete = models.PROTECT
    )   
    
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    