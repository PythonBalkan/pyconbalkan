from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

from pyconbalkan.conference.models import Conference
from pyconbalkan.sponsors.models import Sponsor
from pyconbalkan.sponsors.serializers import SponsorSerializer


class SponsorsViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


def sponsor_view(request, id):
    conference = Conference.objects.filter(active=True)
    sponsor = get_object_or_404(Sponsor, id=id)
    context = {
        'sponsor': sponsor,
        'conference': conference.first() if conference else None,
    }
    return render(request, 'sponsor.html', context)

def sponsors_view(request):
    sponsors = Sponsor.objects.all()
    context = {
        'sponsors': sponsors,
    }
    return render(request, 'sponsors.html', context)