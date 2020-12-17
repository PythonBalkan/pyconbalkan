from django.db import models
from django.db.models import CASCADE
from embed_video.fields import EmbedVideoField
from slugify import slugify

from pyconbalkan.conference.models import AbstractConference
from pyconbalkan.core.models import Person, ActiveModel


class Speaker(Person):
    def __str__(self):
        return self.name

    @property
    def slugify(self):
        return slugify(self.name)

    @property
    def preffered_talk_type(self):
        return self.presentations.order_by("type").first().get_type_display().lower()

    class Meta:
        ordering = ('full_name',)


class YouTubeLink(models.Model):
    speaker = models.ForeignKey(Speaker, related_name="videos", on_delete=models.CASCADE)
    video = EmbedVideoField()


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images', on_delete=CASCADE)
    profile_picture = models.ImageField(upload_to="speakers/profile_picture", blank=True)
