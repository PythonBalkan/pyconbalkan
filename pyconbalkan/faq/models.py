from django.db import models

from pyconbalkan.core.models import ActiveModel


class Faq(ActiveModel):
    question = models.CharField(null=True, blank=True, max_length=100)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question
