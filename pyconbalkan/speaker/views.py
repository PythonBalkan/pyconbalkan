from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from pyconbalkan.speaker.models import Speaker
from pyconbalkan.speaker.serializers import SpeakerSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, active=True, slug=slug)
    context = {
        'speaker': speaker,
    }
    return render(request, 'speaker.html', context)


def speaker_list(request):
    speakers = Speaker.objects.filter(active=True).prefetch_related('presentation')
    context = {
        'speakers': speakers,
    }
    return render(request, 'speakers.html', context)
