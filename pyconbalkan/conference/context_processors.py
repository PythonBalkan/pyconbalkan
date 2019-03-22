import datetime

from pyconbalkan.conference.models import Conference


def previous_conferences(request):
    return {
        'current_conferences': Conference.objects.filter(year__lte=datetime.datetime.now().year),
        'previous_conferences': Conference.objects.filter(year__lt=datetime.datetime.now().year),
    }