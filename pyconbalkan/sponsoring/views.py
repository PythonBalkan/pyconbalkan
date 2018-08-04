from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from pyconbalkan.sponsoring.serializers import SponsoringSerializer
from pyconbalkan.sponsoring.models import Sponsoring
from django.shortcuts import render
from .models import SponsoringForm


class SponsoringViewSet(viewsets.ModelViewSet):
    queryset = Sponsoring.objects.all()
    serializer_class = SponsoringSerializer
    permission_classes = [AllowAny]


def sponsoring_view(request):
    context = {}
    if request.method == 'POST':
        form = SponsoringForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = 'Thank you for taking the part in PyCon Balkan 2018! '
            form = SponsoringForm()
    else:
        form = SponsoringForm()
    context['form'] = form
    return render(request, 'sponsoring.html', context)
