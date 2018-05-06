from django.contrib import admin

from pyconbalkan.organizers.models import Volunteer, VolunteerPhoto


class VolunteerImageInline(admin.TabularInline):
    model = VolunteerPhoto

class VolunteerAdmin(admin.ModelAdmin):
    inlines = [VolunteerImageInline]


admin.site.register(Volunteer, VolunteerAdmin)