from pyconbalkan.conference.models import Conference


def conference(request):
    conference = Conference.objects.filter(active=True)

    return {
        'conference': conference.first() if conference else None
    }