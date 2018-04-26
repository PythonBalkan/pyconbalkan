from django.contrib import admin

from pyconbalkan.conference.models import Conference, CountDown


class ConferenceAdmin(admin.ModelAdmin):
    class Meta:
        model = Conference


class CountDownAdmin(admin.ModelAdmin):
    class Meta:
        model = CountDown


admin.site.register(Conference, ConferenceAdmin)
admin.site.register(CountDown, CountDownAdmin)
