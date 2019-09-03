from collections import defaultdict

from django.db.models import Prefetch
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
    presentations = speaker.presentations.filter(active=True).prefetch_related('conference').order_by('-conference__year')
    conf = defaultdict(list)
    for presentation in presentations:
        conf[presentation.conference.name].append(presentation)

    context = {
        'speaker': speaker,
        'conf': dict(conf)
    }
    return render(request, 'speaker.html', context)


def presentation_list(request, year=None):
    year = year or timezone.now().year

    speakers = Speaker.objects.all().prefetch_related(
        Prefetch(
            "presentations",
            queryset=Presentation.objects.filter(active=True, conference__year=year).order_by("type")
        )
    )
    context = {
        'speakers': speakers,
    }
    return render(request, 'speakers.html', context)
