from django.contrib import admin

from pyconbalkan.conference.models import Conference


class ConferenceAdmin(admin.ModelAdmin):
    class Meta:
        model = Conference


admin.site.register(Conference, ConferenceAdmin)
