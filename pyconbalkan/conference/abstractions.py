from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pyconbalkan.conference.models import Conference


def _get_default_conference():
    if Conference.objects.exists():
        return Conference.objects.first().id


class AbstractConference(models.Model):
    conference = models.ForeignKey(
        Conference, on_delete=models.CASCADE, default=_get_default_conference
    )

    class Meta:
        abstract = True


class ConferenceFilter(admin.SimpleListFilter):
    title = _('Conference year')
    parameter_name = 'conference'

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() is lookup or self.value() == str(lookup),
                'query_string': changelist.get_query_string(
                    {self.parameter_name: lookup}
                ),
                'display': title,
            }

    def lookups(self, request, model_admin):
        choices = []
        for _ in Conference.objects.all():
            if _ == request.conference:
                choices.append((None, "{} Current".format(_)))
            else:
                choices.append((_.id, str(_)))
        return choices

    def queryset(self, request, queryset):
        return queryset.filter(conference=self.value() or request.conference.pk)


class ConferenceAbstractAdmin(admin.ModelAdmin):
    list_filter = (ConferenceFilter,)
