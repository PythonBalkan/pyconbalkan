from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from pyconbalkan.sponsors.models import Sponsor
from pyconbalkan.sponsors.serializers import SponsorSerializer


class SponsorsViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


def sponsor_view(request, id):
    sponsor = get_object_or_404(Sponsor, id=id)
    context = {
        'sponsor': sponsor,
    }
    return render(request, 'sponsor.html', context)


def sponsors_view(request):
    sponsors = Sponsor.objects.all()
    context = {
        'sponsors': sponsors,
    }
    return render(request, 'sponsors.html', context)