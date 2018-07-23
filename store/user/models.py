from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(
        max_length=11, verbose_name='Личный номер', blank=True)
    
    def __str__(self):
        return '{} {} {} {}'.format(self.username, self.first_name, self.last_name, self.phone_number)