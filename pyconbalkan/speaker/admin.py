from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from pyconbalkan.speaker.models import Speaker, SpeakerPhoto, YouTubeLink
from pyconbalkan.timetable.models import Presentation


class SpeakerImageInline(admin.TabularInline):
    model = SpeakerPhoto


class SpeakerYoutubeInline(admin.TabularInline):
    model = YouTubeLink


@admin.register(Speaker)
class SpeakerAdmin(MarkdownxModelAdmin):
    inlines = (SpeakerYoutubeInline,SpeakerImageInline,)
    search_fields = ('full_name',)
