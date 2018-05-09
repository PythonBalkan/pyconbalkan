from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.conference.models import Conference
from pyconbalkan.organizers.models import Volunteer
from pyconbalkan.organizers.serializers import VolunteerSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


def organizers_view(request):
    volunteers = Volunteer.objects.filter(type=Volunteer.VOLUNTEER, active=True)
    organizers = Volunteer.objects.filter(type=Volunteer.ORGANIZER, active=True)
    conference = Conference.objects.filter(active=True)
    context = {
        'volunteers': volunteers,
        'organizers': organizers,
        'conference': conference.first() if conference else None,
    }
    return render(request, 'organizers.html', context)