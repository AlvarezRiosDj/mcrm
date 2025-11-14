from django.db import models

class Email(models.Model):
    
    host = models.CharField(
        max_length = 100,
    )
    email = models.EmailField(
        max_length = 100,
    )
    password = models.CharField(
        max_length = 100,
    )
    smtp_server = models.CharField(
        max_length = 100,
        blank = True, null = True
    )
    smtp_port = models.SmallIntegerField(
        blank = True, null = True
    )
    smtp_verified = models.BooleanField(default=False)
    imap_server = models.CharField(
        max_length = 100,
        blank = True, null = True
    )
    imap_port = models.SmallIntegerField(
        blank = True, null = True
    )
    imap_verified = models.BooleanField(default=False)
    pop3_server = models.CharField(
        max_length = 100,
        blank = True, null = True
    )
    pop3_port = models.SmallIntegerField(
        blank = True, null = True
    )
    pop3_verified = models.BooleanField(default=False)
    use_tls = models.BooleanField(default=False)
    use_ssl = models.BooleanField(default=False)
    last_sync = models.DateTimeField(blank = True, null = True)
    
    
    
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    