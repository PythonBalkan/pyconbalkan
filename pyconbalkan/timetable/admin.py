from django.contrib import admin

from pyconbalkan.conference.abstractions import ConferenceAbstractAdmin
from pyconbalkan.timetable.models import Presentation, Room, Slot


@admin.register(Presentation)
class PresentationAdmin(ConferenceAbstractAdmin):
    autocomplete_fields = ("speaker",)
    list_display = ("type", "title", "speaker", "tag_list", "active")
    list_editable = ("active",)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    pass
