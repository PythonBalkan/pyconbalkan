from rest_framework import viewsets

from pyconbalkan.speaker.models import Speaker
from pyconbalkan.speaker.serializers import SpeakerSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
