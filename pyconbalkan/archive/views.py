from django.shortcuts import render, get_object_or_404


# Create your views here.
from pyconbalkan.conference.models import Conference


def archive_detail(request, year):
    conference = get_object_or_404(Conference, year=year)
    context = {
        'conference': conference,
    }
    return render(request, 'archive.html', context)
