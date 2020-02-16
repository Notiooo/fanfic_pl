from django.db import models
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.conf import settings

class Fandom(models.Model):
    fandom_name = models.CharField(max_length=70, blank=False, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=80)
    tags = TaggableManager(help_text="Podaj słowa kluczowe, które najbardziej oddają twój fandom.")

    def __str__(self):
        return self.fandom_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fandom_name)
        super(Fandom, self).save(*args, **kwargs)

class Fanfic(models.Model):
    fandom = models.ForeignKey(Fandom, on_delete=models.CASCADE, related_name='fanfics')
    title = models.CharField(max_length=160, blank=False)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    nsfw = models.BooleanField(default=False, help_text="Czy fanfic zawiera treści przeznaczone dla osób dorosłych?")
    public = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    tags = TaggableManager(help_text="Podaj słowa kluczowe, które najbardziej oddają twój fanfic.")

    def __str__(self):
        return self.title