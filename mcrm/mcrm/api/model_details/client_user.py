from django.db import models

from django.contrib.auth.models import User

class ClientUser(models.Model):
    
    first_name = models.CharField(
        max_length = 100,
    )
    last_name = models.CharField(
        max_length = 100,
    )
    
    client = models.ForeignKey(
        User,
        on_delete = models.PROTECT
    )
    
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    