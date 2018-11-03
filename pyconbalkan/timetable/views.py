from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.timetable.models import Presentation, Room, Slot, Timetable
from pyconbalkan.timetable.serializers import TimetableSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer


def timetable_view(request):
    slots = Slot.objects.all()
    rooms = Room.objects.all()
    context = {'slots': slots, 'rooms': rooms}
    return render(request, 'timetable.html', context)
