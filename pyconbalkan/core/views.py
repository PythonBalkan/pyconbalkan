from django.shortcuts import render

from pyconbalkan.conference.models import Conference, CountDown
from pyconbalkan.organizers.models import Volunteer
from pyconbalkan.speaker.models import Speaker


def get_conference_context(context):
    conference = Conference.objects.filter(active=True)
    if conference:
        context['conference'] = conference.first()
    return context

def home(request):
    count_down = CountDown.objects.filter(active=True)
    context = {
        'speakers': Speaker.objects.filter(active=True),
        'count_down': count_down.first() if count_down else None,
    }
    get_conference_context(context)
    return render(request, 'home.html', context)


def organizers(request):
    context = {
        'volunteers': Volunteer.objects.filter(type=Volunteer.VOLUNTEER, active=True),
        'organizers': Volunteer.objects.filter(type=Volunteer.ORGANIZER, active=True),
    }
    get_conference_context(context)
    return render(request, 'organizers.html', context)


def sponsors(request):
    context = {}
    get_conference_context(context)
    return render(request, 'sponsors.html', context)


def cfp(request):
    context = {}
    get_conference_context(context)
    return render(request, 'cfp.html', context)