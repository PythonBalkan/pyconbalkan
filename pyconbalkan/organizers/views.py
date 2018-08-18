from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

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


def organizers_list(request):
    volunteers = Volunteer.objects.filter(type=Volunteer.VOLUNTEER, active=True)
    organizers = Volunteer.objects.filter(type=Volunteer.ORGANIZER, active=True)
    context = {
        'volunteers': volunteers,
        'organizers': organizers,
    }
    return context
