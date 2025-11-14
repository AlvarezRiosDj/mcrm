import random
import string
from django.utils import timezone

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

from urllib.parse import urlparse, urlunparse

def rename_docfile(instance, filename):
    current_datetime = timezone.now()    
    formatted_date = current_datetime.strftime('%Y/%m/%d')
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(5))
    
    return f'avatar/{formatted_date}/{result_str}_{filename}'



class Profile(models.Model):

    cel = models.CharField(
        max_length = 100,
        blank = True, null = True,
    )
    avatar = models.ImageField(
        upload_to = rename_docfile,
        blank = True, null = True,
    )
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
    )