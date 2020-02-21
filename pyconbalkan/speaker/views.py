from collections import defaultdict

from django.db.models import Prefetch, Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import truncatewords
from django.utils import timezone
from django.utils.html import strip_tags
from meta.views import Meta
from rest_framework import viewsets

from pyconbalkan.conference.models import Conference
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.speaker.serializers import SpeakerSerializer
from pyconbalkan.timetable.models import Presentation


class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


def speaker_detail(request, slug=None):
    if slug:
        q = Q(slug=slug)
    elif "pk" in request.GET.keys():
        q = Q(pk=request.GET['pk'])
    else:
        raise Http404()

    speaker = get_object_or_404(Speaker, q)
    presentations = speaker.presentations.filter(active=True).prefetch_related('conference').order_by('-conference__year')
    conf = defaultdict(list)
    for presentation in presentations:
        conf[presentation.conference.year].append(presentation)

    speaker_image = speaker.images.all().first().profile_picture.url if speaker.images.exists() else None

    most_recent_year = list(conf.keys())[0]

    context = {
        'speaker': speaker,
        'conf': dict(conf),
        'meta': Meta(
            description=truncatewords(strip_tags(speaker.description), 20),
            image=speaker_image,
            title=f"{speaker.full_name} @ PyCon Balkan {most_recent_year}"
        )

    }
    return render(request, 'speaker.html', context)


def presentation_list(request, year=None):
    conference = get_object_or_404(Conference, year=year or timezone.now().year)
    presentations = Presentation.objects.filter(active=True, conference__year=year).order_by("type")
    speakers = Speaker.objects.all().prefetch_related(
        Prefetch(
            "presentations",
            queryset=presentations
        )
    )
    speakers = filter(lambda speaker: any(speaker.presentations.all()), speakers)

    presentation_count = presentations.count()

    context = {
        'speakers': speakers,
        'meta': Meta(
            description=f"This year we will be hosting {presentation_count} presentations including"
                        f" talks, keynotes as well as workshops at {conference}."
                        f" Follow this link to get more details !",
            title=f"{conference} - Speakers",
            image=conference.conference_logo.url if conference.conference_logo else None
        )
    }
    return render(request, 'speakers.html', context)
