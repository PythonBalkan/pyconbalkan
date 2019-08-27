from django.contrib import admin

from pyconbalkan.conference.abstractions import ConferenceAbstractAdmin
from pyconbalkan.timetable.models import Timetable, Presentation, Room, Slot


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    pass


@admin.register(Presentation)
class PresentationAdmin(ConferenceAbstractAdmin):
    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    pass
