from django.db import models
from pyconbalkan.core.models import ActiveModel
from pyconbalkan.speaker.models import Speaker
from django.db.models import CASCADE


class Timetable(ActiveModel):
    title = models.CharField(null=True, blank=True, max_length=100)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Presentation(ActiveModel):
    TALK = 0
    WORKSHOP = 1
    PRESENTATION_TYPE = (
        (TALK, 'Talk'),
        (WORKSHOP, 'Workshop'),
    )

    title = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.IntegerField(choices=PRESENTATION_TYPE, default=TALK)

    speaker = models.ForeignKey(Speaker, blank=True, null=True, related_name='presentation', on_delete=CASCADE)

    def __str__(self):
        return '[{}] {}'.format(self.get_type_display(), self.title)


class Room(ActiveModel):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name


class Slot(ActiveModel):
    from_date = models.DateTimeField(null=True, blank=True)
    to_date = models.DateTimeField(null=True, blank=True)

    timetable = models.ForeignKey(Timetable, blank=True, null=True, related_name='slot', on_delete=CASCADE)
    talk = models.ForeignKey(Presentation, blank=True, null=True, related_name='slot', on_delete=CASCADE)
    room = models.ForeignKey(Room, blank=True, null=True, related_name='slot', on_delete=CASCADE)

    def __str__(self):
        return 'From {:%d-%m-%Y %H:%M} to {:%d-%m-%Y %H:%M}'.format(self.from_date, self.to_date)
