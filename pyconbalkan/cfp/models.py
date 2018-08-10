import random
import string
from statistics import median, StatisticsError

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import CASCADE
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from slugify import slugify
from taggit.managers import TaggableManager
from . import const


class Cfp(models.Model):
    name = models.CharField(max_length=256)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    personal_website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=1024)
    description = MarkdownxField()
    accepted = models.BooleanField(default=False)
    slug = models.CharField(unique=True, blank=True, max_length=100)
    type = models.IntegerField(choices=const.TYPE_CFP, default=const.TALK)
    duration = models.CharField(max_length=100, null=True)

    @property
    def rating(self):
        try:
            return median(self.ratings.all().values_list('mark', flat=True))
        except StatisticsError:
            return "N/A"

    def __str__(self):
        return '{}: "{}" by {} - [{}]'.format(self.get_type_display(), self.title, self.name, 'Accepted' if self.accepted else 'Pending')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('{}-{}'.format(self.name, self.title))
            if Cfp.objects.filter(slug=self.slug):
                self.slug = '{}-{}-{}'.format(slugify(self.name), slugify(self.title), ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)))
        super(Cfp, self).save(*args, **kwargs)


class CFPRating(models.Model):
    mark = models.IntegerField(validators=[MaxValueValidator(10, "Maximum rating is 10"), MinValueValidator(1, "Minimum Rating is 1")])
    cfp = models.ForeignKey(Cfp, related_name="ratings", on_delete=CASCADE)
    user = models.ForeignKey(getattr(settings, "AUTH_USER_MODEL"), on_delete=CASCADE)
    comment = MarkdownxField(blank=True, null=True)
    tags = TaggableManager(blank=True)

    class Meta:
        unique_together = (("user", "cfp",),)

    @property
    def formatted_markdown(self):
        if self.comment:
            return markdownify(self.comment)
        return ''

    def __str__(self):
        return '[{}] by {}'.format(self.mark, self.user.first_name)

