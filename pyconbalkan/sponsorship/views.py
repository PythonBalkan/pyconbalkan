from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.sponsorship.models import Sponsorship
from pyconbalkan.sponsorship.serializers import SponsorshipSerializer
from pyconbalkan.coc.views import coc_view


class SponsorshipViewSet(viewsets.ModelViewSet):
    queryset = Sponsorship.objects.all()
    serializer_class = SponsorshipSerializer


def sponsorship_view(request):
    sponsorship = Sponsorship.objects.filter(active=True)
    context = {
        'sponsorship': sponsorship.first() if sponsorship else None,
    }
    return render(request, 'sponsorship.html', context)
