from django.contrib import admin

from pyconbalkan.conference.abstractions import ConferenceAbstractAdmin
from pyconbalkan.conference.models import Conference, CountDown, MissionStatement
from markdownx.admin import MarkdownxModelAdmin


class ConferenceAdmin(admin.ModelAdmin):
    class Meta:
        model = Conference


class CountDownAdmin(ConferenceAbstractAdmin):
    class Meta:
        model = CountDown


class MissionStatementAdmin(ConferenceAbstractAdmin, MarkdownxModelAdmin):
    class Meta:
        model = MissionStatement


admin.site.register(Conference, ConferenceAdmin)
admin.site.register(CountDown, CountDownAdmin)
admin.site.register(MissionStatement, MissionStatementAdmin)