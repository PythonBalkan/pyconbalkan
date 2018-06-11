from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from pyconbalkan.organizers.models import Volunteer, VolunteerPhoto


class VolunteerImageInline(admin.TabularInline):
    model = VolunteerPhoto

class VolunteerAdmin(MarkdownxModelAdmin):
    inlines = [VolunteerImageInline]


admin.site.register(Volunteer, VolunteerAdmin)