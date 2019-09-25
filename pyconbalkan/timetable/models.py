from django.db import models
from markdownx.models import MarkdownxField
from slugify import slugify
from taggit.managers import TaggableManager

from pyconbalkan.conference.models import AbstractConference
from pyconbalkan.core.models import ActiveModel
from pyconbalkan.speaker.models import Speaker
from django.db.models import CASCADE


class Presentation(AbstractConference, ActiveModel):
    TALK = 10  # 0
    WORKSHOP = 15  # 1
    KEYNOTE = 5  # 2
    PRESENTATION_TYPE = (
        (TALK, 'Talk'),
        (WORKSHOP, 'Workshop'),
        (KEYNOTE, 'Keynote'),
    )

    PRESENTATION_TYPE_REVERSE = {
        'Talk': TALK,
        'Workshop': WORKSHOP,
        'Keynote': KEYNOTE
    }

    title = models.CharField(null=True, blank=True, max_length=100)
    description = MarkdownxField(null=True, blank=True)
    type = models.IntegerField(choices=PRESENTATION_TYPE, default=TALK)
    tags = TaggableManager()
    speaker = models.ForeignKey(Speaker, blank=True, null=True, related_name='presentations', on_delete=CASCADE)
    youtube = models.URLField(null=True, blank=True)

    @property
    def slugify(self):
        return slugify(self.title)

    @property
    def slugify_speaker(self):
        if self.speaker:
            return slugify(self.speaker.name)

    def __str__(self):
        return '[{}] {}'.format(self.get_type_display(), self.title)


class Room(AbstractConference, ActiveModel):
    name = models.CharField(null=True, blank=True, max_length=100)
    sort_order = models.IntegerField()

    def __str__(self):
        return self.name


class Slot(AbstractConference, ActiveModel):
    from_date = models.DateTimeField(null=True, blank=True)
    to_date = models.DateTimeField(null=True, blank=True)

    talk = models.ForeignKey(Presentation, blank=True, null=True, related_name='slot', on_delete=CASCADE)
    room = models.ForeignKey(Room, blank=True, null=True, related_name='slot', on_delete=CASCADE)

    def __str__(self):
        return 'From {:%d-%m-%Y %H:%M} to {:%d-%m-%Y %H:%M}'.format(self.from_date, self.to_date)
