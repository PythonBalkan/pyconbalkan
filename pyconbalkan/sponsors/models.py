from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class SponsorshipLevel(DjangoChoices):
    keystone = ChoiceItem('Keystone')
    platinum = ChoiceItem('Platinum')
    gold = ChoiceItem('Gold')
    silver = ChoiceItem('Silver')
    partner = ChoiceItem('Partner')


class Sponsor(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    level = models.CharField(max_length=16, choices=SponsorshipLevel.choices)
    logo = models.ImageField(upload_to='static/img/sponsors')
