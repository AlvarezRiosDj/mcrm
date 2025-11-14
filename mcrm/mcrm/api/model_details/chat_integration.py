from django.db import models

from django.contrib.auth.models import User
from .chat_type import ChatType

class ChatIntegration(models.Model):
    
    name = models.CharField(
        max_length = 100,
    )
    access = models.JSONField(
        blank = True, null = True
    )
    chat_type = models.ForeignKey(
        ChatType,
        on_delete = models.PROTECT
    )
    client = models.ForeignKey(
        User,
        on_delete = models.PROTECT
    )    
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)