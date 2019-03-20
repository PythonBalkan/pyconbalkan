from django.db import models
from markdownx.models import MarkdownxField
from pyconbalkan.core.models import SingleActiveModel
from django.utils.text import slugify


class CodeOfConduct(SingleActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    description = MarkdownxField(null=True, blank=True)

    def __str__(self):
        return self.title


class ResponseGuide(SingleActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    description = MarkdownxField(null=True, blank=True)
    slug = models.CharField(unique=True, blank=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ResponseGuide, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
