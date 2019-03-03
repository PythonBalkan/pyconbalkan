from django.db import models
from pyconbalkan.conference.models import Conference


class AbstractConference(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    class Meta:
        abstract = True