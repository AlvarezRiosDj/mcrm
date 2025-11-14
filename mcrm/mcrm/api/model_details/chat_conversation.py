from django.db import models


from .chat_integration import ChatIntegration
from .client_user import ClientUser

class ChatConversation(models.Model):
    
    name = models.CharField(
        max_length = 100,
    )
    chat_integration = models.ForeignKey(
        ChatIntegration,
        on_delete = models.PROTECT
    )
    participants = models.ForeignKey(
        ClientUser,
        on_delete = models.PROTECT
    )
    admins = models.ForeignKey(
        ClientUser,
        on_delete = models.PROTECT
    )
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    