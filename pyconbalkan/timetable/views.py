from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.timetable.models import Presentation, Room, Slot, Timetable
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
    slots = Slot.objects.all().order_by('from_date')
    rooms = Room.objects.all()
    context = {'slots': slots, 'rooms': rooms, 'DAYS': DAYS}
    return render(request, 'timetable.html', context)
