from django.db import models
from markdownx.models import MarkdownxField

from pyconbalkan.core.models import ActiveModel


class Faq(ActiveModel):
    question = models.CharField(null=True, blank=True, max_length=100)
    answer = MarkdownxField(null=True, blank=True)

    def __str__(self):
        return self.question
