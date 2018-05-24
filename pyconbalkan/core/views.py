from django.shortcuts import render

from pyconbalkan.conference.models import Conference, CountDown
from pyconbalkan.speaker.models import Speaker


def home(request):
    conference = Conference.objects.filter(active=True)
    count_down = CountDown.objects.filter(active=True)
    speakers = Speaker.objects.filter(active=True)
    context = {
        'speakers': speakers,
        'conference': conference.first() if conference else None,
        'count_down': count_down.first() if count_down else None,
    }
    return render(request, 'home.html', context)


def tickets(request):
    conference = Conference.objects.filter(active=True)
    context = {
        'conference': conference.first() if conference else None,
    }
    return render(request, 'tickets.html', context)
