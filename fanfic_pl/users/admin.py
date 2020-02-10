from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models, forms

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    model = models.CustomUser
    list_display = ['email', 'username',]

admin.site.register(models.CustomUser)