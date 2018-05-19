from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=256)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
