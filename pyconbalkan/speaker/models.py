from django.db import models
from django.db.models import CASCADE

from pyconbalkan.core.models import Person, ActiveModel
from markdownx.models import MarkdownxField


class Speaker(ActiveModel, Person):
    keynote = models.BooleanField(default=False)
    talk_excerpt = MarkdownxField(null=True, blank=True)


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images', on_delete=CASCADE)
    profile_picture = models.ImageField(upload_to="speakers/profile_picture", blank=True)
