from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from pyconbalkan.speaker.models import Speaker, SpeakerPhoto
from pyconbalkan.timetable.models import Presentation


class SpeakerImageInline(admin.TabularInline):
    model = SpeakerPhoto


@admin.register(Speaker)
class SpeakerAdmin(MarkdownxModelAdmin):
    inlines = (SpeakerImageInline,)
    search_fields = ('full_name',)
