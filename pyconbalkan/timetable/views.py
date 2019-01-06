
from django.shortcuts import render, redirect
from rest_framework import viewsets

from pyconbalkan.conference.models import Conference
from pyconbalkan.timetable.models import Room, Slot, Timetable
from pyconbalkan.timetable.serializers import TimetableSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


def timetable_pdf_view(request):

    conference = request.conference
    if conference and conference.timetable_pdf:
        return redirect(conference.timetable_pdf.url)
    return redirect('/')


def timetable_view(request):
    slots_by_rooms = {}
    rooms = Room.objects.all()
    slots = Slot.objects.all()
    slots_order_by_date = slots.order_by('from_date')
    for room in rooms:
        slots_by_rooms[room.name] = slots_order_by_date.filter(room=room)
    days_count = 0
    DAYS = {}
    for slot in slots:
        if slot.from_date.date() not in DAYS:
            DAYS[slot.from_date.date()] = 'Day {}'.format(days_count + 1)
            days_count += 1
    context = {
        'slots': slots_order_by_date,
        'slots_by_rooms': slots_by_rooms,
        'rooms': rooms,
        'DAYS': DAYS
    }
    return render(request, 'timetable.html', context)
