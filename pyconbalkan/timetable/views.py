from rest_framework import viewsets
from pyconbalkan.timetable.models import Timetable, Presentation, Room
from pyconbalkan.timetable.serializers import TimetableSerializer
from django.shortcuts import render


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer  


def timetable_view(request):
    presentations = Presentation.objects.all()
    rooms = Room.objects.all()
    context = {'presentations': presentations, 'rooms': rooms}
    return render(request, 'timetable.html', context)
