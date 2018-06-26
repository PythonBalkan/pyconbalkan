from django.db import models
from markdownx.models import MarkdownxField
from pyconbalkan.core.models import SingleActiveModel


class CodeOfConduct(SingleActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    description = MarkdownxField(null=True, blank=True)

    def __str__(self):
        return self.title


class ResponseGuide(SingleActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    description = MarkdownxField(null=True, blank=True)
    slug = models.CharField(unique=True, blank=True, max_length=100)

    def __str__(self):
        return self.title
