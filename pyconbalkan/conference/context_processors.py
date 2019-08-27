import datetime

from pyconbalkan.conference.models import Conference
from pyconbalkan.sponsors.models import Sponsor


def previous_conferences(request):
    return {
        'sidebar_sponsors': Sponsor.objects.filter(sidebar=True, active=True),
        'current_conferences': Conference.objects.filter(year__lte=datetime.datetime.now().year),
        'previous_conferences': Conference.objects.filter(year__lt=datetime.datetime.now().year),
    }