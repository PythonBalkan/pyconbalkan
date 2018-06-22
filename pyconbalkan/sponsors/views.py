from django.shortcuts import render
from rest_framework import viewsets
from pyconbalkan.sponsors.models import Sponsor
from pyconbalkan.sponsors.serializers import SponsorSerializer


class SponsorsViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


def sponsors_view(request):
    sponsors = Sponsor.objects.all()
    context = {'sponsors': sponsors}
    return render(request, 'sponsors.html', context)
