from django.db import models
from django.db.models import CASCADE

from pyconbalkan.core.models import Person, ActiveModel


class Speaker(ActiveModel, Person):
    pass


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images', on_delete=CASCADE)
    profile_picture = models.ImageField(upload_to="static/img")
