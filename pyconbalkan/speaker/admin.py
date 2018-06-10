from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from pyconbalkan.speaker.models import Speaker, SpeakerPhoto


class SpeakerImageInline(admin.TabularInline):
    model = SpeakerPhoto


class SpeakerAdmin(MarkdownxModelAdmin):
    inlines = [SpeakerImageInline]


admin.site.register(Speaker, SpeakerAdmin)
