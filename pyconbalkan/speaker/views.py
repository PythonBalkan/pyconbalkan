from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import viewsets

from pyconbalkan.speaker.models import Speaker
from pyconbalkan.speaker.serializers import SpeakerSerializer
from pyconbalkan.timetable.models import Presentation


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {
        'speaker': speaker,
    }
    return render(request, 'speaker.html', context)


def presentation_list(request, year=None):
    year = year or timezone.now().year

    speakers = Speaker.objects.filter(
        presentations__active=True,
        presentations__conference__year=year
    ).prefetch_related('presentations')
    context = {
        'speakers': speakers,
    }
    return render(request, 'speakers.html', context)
