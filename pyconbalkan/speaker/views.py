from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from pyconbalkan.conference.models import Conference
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.speaker.serializers import SpeakerSerializer


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


def speaker_detail(request, slug):
    conference = Conference.objects.filter(active=True)
    speaker = get_object_or_404(Speaker, active=True, slug=slug)
    context = {
        'speaker': speaker,
        'conference': conference.first() if conference else None,
    }
    return render(request, 'speaker.html', context)