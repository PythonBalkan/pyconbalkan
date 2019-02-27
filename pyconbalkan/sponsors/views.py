from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from pyconbalkan.sponsors.forms import SponsoringForm
from pyconbalkan.sponsors.models import Sponsor, Sponsoring, Package, SponsorshipLevel, SponsorConference
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
    keystone_sponsors = SponsorConference.objects.filter(level=SponsorshipLevel.keystone, conference=request.conference).sponsor
    platinum_sponsors = SponsorConference.objects.filter(level=SponsorshipLevel.platinum, conference=request.conference).sponsor
    gold_sponsors = SponsorConference.objects.filter(level=SponsorshipLevel.gold, conference=request.conference).sponsor
    silver_sponsors = SponsorConference.objects.filter(level=SponsorshipLevel.silver, conference=request.conference).sponsor
    partners = SponsorConference.objects.filter(level=SponsorshipLevel.partner, conference=request.conference).sponsor

    context = {
        'keystone_sponsors': keystone_sponsors,
        'platinum_sponsors': platinum_sponsors,
        'gold_sponsors': gold_sponsors,
        'silver_sponsors': silver_sponsors,
        'partners': partners,
    }
    return render(request, 'sponsors.html', context)


@login_required
def sponsoring_view(request):
    packages = Package.objects.filter(active=True)
    context = {
        'packages': packages,
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
