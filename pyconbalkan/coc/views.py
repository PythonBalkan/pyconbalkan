from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from .models import CodeOfConduct, ResponseGuide
from .serializers import CodeOfConductSerializer
from pyconbalkan.conference.models import Conference


class CodeOfConductViewSet(viewsets.ModelViewSet):
    queryset = CodeOfConduct.objects.all()
    serializer_class = CodeOfConductSerializer


def coc_view(request):
    conference = Conference.objects.filter(active=True)
    coc = CodeOfConduct.objects.filter(active=True)
    r_guide = ResponseGuide.objects.filter(active=True)
    context = {
        'coc': coc.first() if coc else None,
        'response_guide': r_guide.first() if r_guide else None,
        'conference': conference.first() if conference else None,
    }
    return render(request, 'coc.html', context)


def response_guide(request, slug):
    r_guide = get_object_or_404(ResponseGuide, active=True, slug=slug)
    context = {
        'response_guide': r_guide
    }
    return render(request, 'response_guide.html', context)
