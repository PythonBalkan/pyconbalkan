from django.db import models
from django_countries.fields import CountryField


class Conference(models.Model):
    INTERNATIONAL = 0
    NATIONAL = 1
    CONF_TYPE = (
        (INTERNATIONAL, 'International'),
        (NATIONAL, 'National'),
    )

    year = models.PositiveIntegerField()
    city = models.CharField(null=True, blank=True, max_length=200)
    country = CountryField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    max_attendees = models.PositiveIntegerField(null=True, blank=True)
    type = models.IntegerField(choices=CONF_TYPE)