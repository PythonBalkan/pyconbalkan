from rest_framework import viewsets
from pyconbalkan.sponsors.models import Sponsor
from pyconbalkan.sponsors.serializers import SponsorSerializer


class SponsorsViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
