from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.speaker.models import Speaker
from pyconbalkan.speaker.serializers import SpeakerSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


def speaker_detail(request, pk):
    speaker = Speaker.objects.get(active=True, pk=pk)
    context = {
        'speaker': speaker
    }
    return render(request, 'speaker.html', context)