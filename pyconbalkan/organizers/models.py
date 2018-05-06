from django.contrib.auth.models import User
from django.db import models

from pyconbalkan.core.models import Person, ActiveModel


class Volunteer(ActiveModel, Person):
    ORGANIZER = 0
    VOLUNTEER = 1
    VOLUNTEER_TYPE = (
        (ORGANIZER, 'Organizer'),
        (VOLUNTEER, 'Volunteer'),
    )

    user = models.ForeignKey(User, blank=True, null=True, related_name='volunteer')
    type = models.IntegerField(choices=VOLUNTEER_TYPE, default=VOLUNTEER)

class VolunteerPhoto(models.Model):
    volunteer = models.ForeignKey(Volunteer, related_name='images')
    profile_picture = models.ImageField(upload_to="static/img")