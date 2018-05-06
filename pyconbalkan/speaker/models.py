from django.db import models

from pyconbalkan.core.models import Person, ActiveModel


class Speaker(ActiveModel, Person):
    pass


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images')
    profile_picture = models.ImageField(upload_to="static/img")
