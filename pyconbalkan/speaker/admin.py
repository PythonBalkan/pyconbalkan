from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from pyconbalkan.conference.abstractions import ConferenceAbstractAdmin
from pyconbalkan.speaker.models import Speaker, SpeakerPhoto


class SpeakerImageInline(admin.TabularInline):
    model = SpeakerPhoto


@admin.register(Speaker)
class SpeakerAdmin(ConferenceAbstractAdmin, MarkdownxModelAdmin):
    inlines = (SpeakerImageInline,)
    search_fields = ('full_name',)
