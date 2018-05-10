from rest_framework import viewsets
from pyconbalkan.timetable.models import Timetable
from pyconbalkan.timetable.serializers import TimetableSerializer


class TimetableViewSet(viewsets.ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer
