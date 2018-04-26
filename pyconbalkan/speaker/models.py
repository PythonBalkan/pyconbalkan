from django.db import models

from pyconbalkan.core.models import SingleActiveModel


class Speaker(SingleActiveModel):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SpeakerPhoto(models.Model):
    speaker = models.ForeignKey(Speaker, related_name='images')
    profile_picture = models.ImageField(upload_to="static/img")
