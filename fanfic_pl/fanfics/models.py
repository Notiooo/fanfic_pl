from django.db import models
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.conf import settings

class Fandom(models.Model):
    fandom_name = models.CharField(max_length=70, blank=False, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, max_length=80)
    tags = TaggableManager()

    def __str__(self):
        return self.fandom_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fandom_name)
        super(Fandom, self).save(*args, **kwargs)

class Fanfic(models.Model):
    fandom = models.ForeignKey(Fandom, on_delete=models.CASCADE, related_name='fandom')
    title = models.CharField(max_length=160, blank=False)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title