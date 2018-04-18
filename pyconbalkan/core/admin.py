from django.apps import AppConfig
from django.contrib import admin

from pyconbalkan.core.models import Speaker, SpeakerPhoto


class CoreConfig(AppConfig):
    name = 'core'


class SpeakerImageInline(admin.TabularInline):
    model = SpeakerPhoto


class SpeakerAdmin(admin.ModelAdmin):
    inlines = [SpeakerImageInline]


admin.site.register(Speaker, SpeakerAdmin)
