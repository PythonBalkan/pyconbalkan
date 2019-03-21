import datetime

from pyconbalkan.conference.models import Conference


def previous_conferences(request):
    return {
        'previous_conferences': Conference.objects.filter(year__lt=datetime.datetime.now().year),
    }