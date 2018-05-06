from django.shortcuts import render

from pyconbalkan.conference.models import Conference, CountDown
from pyconbalkan.organizers.models import Volunteer
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


def organizers(request):
    volunteers = Volunteer.objects.filter(type=Volunteer.VOLUNTEER, active=True)
    organizers = Volunteer.objects.filter(type=Volunteer.ORGANIZER, active=True)
    conference = Conference.objects.filter(active=True)
    context = {
        'volunteers': volunteers,
        'organizers': organizers,
        'conference': conference.first() if conference else None,
    }
    return render(request, 'organizers.html', context)


def sponsor(request):
    return render(request, 'sponsor.html')
