from django.db import models
from django.db.models import CASCADE

from pyconbalkan.conference.models import AbstractConference
from pyconbalkan.core.models import Person, ActiveModel


class Speaker(Person):
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('full_name',)


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images', on_delete=CASCADE)
    profile_picture = models.ImageField(upload_to="speakers/profile_picture", blank=True)
