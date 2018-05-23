from django.contrib import admin
from pyconbalkan.timetable.models import Timetable, Presentation, Room, Slot


class TimetableAdmin(admin.ModelAdmin):
    class Meta:
        model = Timetable


class PresentationAdmin(admin.ModelAdmin):
    class Meta:
        model = Presentation


class RoomAdmin(admin.ModelAdmin):
    class Meta:
        model = Room


class SlotAdmin(admin.ModelAdmin):
    class Meta:
        model = Slot


admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Slot, SlotAdmin)
