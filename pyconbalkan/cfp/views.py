from rest_framework import viewsets
from pyconbalkan.cfp.models import Cfp
from pyconbalkan.cfp.serializers import CfpSerializer


class CfpViewSet(viewsets.ModelViewSet):
    queryset = Cfp.objects.all()
    serializer_class = CfpSerializer
