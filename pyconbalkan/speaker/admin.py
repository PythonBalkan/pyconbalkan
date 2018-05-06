from django.contrib import admin

from pyconbalkan.speaker.models import Speaker, SpeakerPhoto


class SpeakerImageInline(admin.TabularInline):
    model = SpeakerPhoto


class SpeakerAdmin(admin.ModelAdmin):
    inlines = [SpeakerImageInline]


admin.site.register(Speaker, SpeakerAdmin)
