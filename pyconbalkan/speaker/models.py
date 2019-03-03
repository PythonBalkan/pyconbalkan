from django.db import models
from django.db.models import CASCADE

from pyconbalkan.conference.models import AbstractConference
from pyconbalkan.core.models import Person, ActiveModel


class Speaker(AbstractConference, ActiveModel, Person):
    keynote = models.BooleanField(default=False)

    def __str__(self):
        return '{} [{}]'.format(self.name, 'Keynote' if self.keynote else 'Speaker')

    class Meta:
        ordering = ('full_name',)


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images', on_delete=CASCADE)
    profile_picture = models.ImageField(upload_to="speakers/profile_picture", blank=True)
