from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

from pyconbalkan.conference.models import Conference
from pyconbalkan.sponsors.forms import SponsoringForm
from pyconbalkan.sponsors.models import Sponsor, Sponsoring
from pyconbalkan.sponsors.serializers import SponsorSerializer, SponsoringSerializer


class SponsorsViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsoringViewSet(viewsets.ModelViewSet):
    queryset = Sponsoring.objects.all()
    serializer_class = SponsoringSerializer


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


def sponsoring_view(request):
    context = {}
    if request.method == 'POST':
        form = SponsoringForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = 'Thank you for your interest to the part of PyCon Balkan 2018! We will contact you soon.'
            form = SponsoringForm()
    else:
        form = SponsoringForm()
    context['form'] = form
    return render(request, 'sponsoring.html', context)
