from django.db import models


class Cfp(models.Model):
    title = models.CharField(max_length=1024)
    text = models.TextField()

