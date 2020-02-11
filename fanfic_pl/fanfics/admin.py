from django.contrib import admin

from . import models

class FanficsInline(admin.TabularInline):
    model = models.Fanfic

@admin.register(models.Fandom)
class FanficAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('fandom_name',)}
    inlines = [
        FanficsInline,
    ]
