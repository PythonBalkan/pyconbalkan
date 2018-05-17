from django.db import models
from django.db.models import CASCADE
from markdownx.models import MarkdownxField
from pyconbalkan.core.models import Person, ActiveModel


class Speaker(ActiveModel, Person):
    biography = MarkdownxField(null=True, blank=True)


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images', on_delete=CASCADE)
    profile_picture = models.ImageField(upload_to="speakers/profile_picture", blank=True)
