from django.shortcuts import render
from rest_framework import viewsets

from pyconbalkan.about.models import About
from pyconbalkan.about.serializers import AboutSerializer
from pyconbalkan.coc.views import coc_view
from pyconbalkan.organizers.views import organizers_list


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


def about_view(request):
    about = About.objects.filter(active=True)
    context = {
        'about': about.first() if about else None,
    }
    return render(request, 'about.html', context)
