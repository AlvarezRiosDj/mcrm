from django.db import models

from .chat_conversation import ChatConversation
from .client_user import ClientUser

class ChatMessage(models.Model):    
    
    message = models.TextField(
        blank = True, null = True
    )
    chat_conversation = models.ForeignKey(
        ChatConversation,
        on_delete = models.PROTECT
    )
    sender = models.ForeignKey(
        ClientUser,
        on_delete = models.PROTECT
    )
    
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    