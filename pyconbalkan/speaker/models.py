from django.db import models
from django.db.models import CASCADE
from markdownx.models import MarkdownxField

from pyconbalkan.core.models import Person, ActiveModel


class Speaker(ActiveModel, Person):
    keynote = models.BooleanField(default=False)
    description = MarkdownxField(blank=True, default='')


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images', on_delete=CASCADE)
    profile_picture = models.ImageField(upload_to="speakers/profile_picture", blank=True)
