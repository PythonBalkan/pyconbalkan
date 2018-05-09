from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.about.models import About
from pyconbalkan.about.serializers import AboutSerializer
from pyconbalkan.conference.models import Conference


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


def about_view(request):
    conference = Conference.objects.filter(active=True)
    about = About.objects.filter(active=True)
    context = {
        'about': about.first() if about else None,
        'conference': conference.first() if conference else None,
    }
    return render(request, 'about.html', context)
