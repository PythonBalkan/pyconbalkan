from django.db import models

from pyconbalkan.conference.context import singleton


class ConferenceManager(models.Manager):
    def get_queryset(self):
        if hasattr(singleton, "conference"):
            return (
                super(ConferenceManager, self)
                .get_queryset()
                .filter(conference=singleton.conference)
            )
        else:
            return super(ConferenceManager, self).get_queryset()
