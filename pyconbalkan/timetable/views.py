from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.timetable.models import Room, Slot, Timetable
from pyconbalkan.timetable.serializers import TimetableSerializer
from datetime import datetime

DAYS = {
    datetime.strptime('16Nov2018', '%d%b%Y').date(): 'Day 1',
    datetime.strptime('17Nov2018', '%d%b%Y').date(): 'Day 2',
    datetime.strptime('18Nov2018', '%d%b%Y').date(): 'Day 3',
}


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


def timetable_view(request):
    slots_by_rooms = {}

    rooms = Room.objects.all()
    slots = Slot.objects.all()
    slots_order_by_date = slots.order_by('from_date')
    for room in rooms:
        slots_by_rooms[room.name] = slots_order_by_date.filter(room=room)
    context = {
        'slots': slots_order_by_date,
        'slots_by_rooms': slots_by_rooms,
        'rooms': rooms,
        'DAYS': DAYS
    }
    return render(request, 'timetable.html', context)
