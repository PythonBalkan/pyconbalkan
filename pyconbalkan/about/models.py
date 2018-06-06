from django.db import models
from markdownx.models import MarkdownxField

from pyconbalkan.core.models import SingleActiveModel


class About(SingleActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    description = MarkdownxField(null=True, blank=True)

    def __str__(self):
        return self.title