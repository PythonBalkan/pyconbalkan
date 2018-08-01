from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from pyconbalkan.conference.models import Conference
from pyconbalkan.organizers.models import Volunteer
from pyconbalkan.organizers.serializers import VolunteerSerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


def organizer_view(request, slug):
    organizer = get_object_or_404(Volunteer, slug=slug)
    context = {
        'organizer': organizer,
    }
    return render(request, 'organizer.html', context)


def organizers_listview(request):
    volunteers = Volunteer.objects.filter(type=Volunteer.VOLUNTEER, active=True).order_by('full_name')
    organizers = Volunteer.objects.filter(type=Volunteer.ORGANIZER, active=True).order_by('full_name')
    conference = Conference.objects.filter(active=True)
    context = {
        'volunteers': volunteers,
        'organizers': organizers,
        'conference': conference.first() if conference else None,
    }
    return render(request, 'organizers.html', context)