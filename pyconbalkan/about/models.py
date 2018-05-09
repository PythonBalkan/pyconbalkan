from django.db import models

from pyconbalkan.core.models import SingleActiveModel


class About(SingleActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title