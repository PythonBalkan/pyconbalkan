from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from pyconbalkan.sponsors.forms import SponsoringForm
from pyconbalkan.sponsors.models import Sponsor, Sponsoring, Package, SponsorshipLevel
from pyconbalkan.sponsors.serializers import SponsorSerializer, SponsoringSerializer


class SponsorsViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


class SponsoringViewSet(viewsets.ModelViewSet):
    queryset = Sponsoring.objects.all()
    serializer_class = SponsoringSerializer


def sponsor_view(request, id):
    sponsor = get_object_or_404(Sponsor, id=id)
    context = {
        'sponsor': sponsor,
    }
    return render(request, 'sponsor.html', context)


def sponsors_view(request):
    conference = Conference.objects.filter(active=True)

    keystone_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.keystone)
    platinum_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.platinum)
    gold_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.gold)
    silver_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.silver)
    partners = Sponsor.objects.filter(level=SponsorshipLevel.partner)
    context = {
        'keystone_sponsors': keystone_sponsors,
        'platinum_sponsors': platinum_sponsors,
        'gold_sponsors': gold_sponsors,
        'silver_sponsors': silver_sponsors,
        'partners': partners,
        'conference': conference.first() if conference else None,
        'meta': conference.first().as_meta(),
    }
    return render(request, 'sponsors.html', context)


def sponsoring_view(request):
    conference = Conference.objects.filter(active=True)
    packages = Package.objects.filter(active=True)
    Sponsor.objects
    context = {
        'packages': packages,
        'conference': conference.first() if conference else None,
        'meta': conference.first().as_meta(),
    }
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
