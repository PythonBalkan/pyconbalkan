from rest_framework import viewsets

from pyconbalkan.conference.models import Conference
from pyconbalkan.conference.serializers import ConferenceSerializer


class ConferenceViewSet(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
