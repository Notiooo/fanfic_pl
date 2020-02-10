from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.

class CustomUser(AbstractUser):
    birth = models.DateField(null=True, blank=True, help_text='DD.MM.RR - na przykład 21.01.1999')
    about = models.CharField(max_length=150, blank=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})