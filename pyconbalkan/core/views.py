from django.db.models import Q
from django.shortcuts import render

from pyconbalkan.conference.models import CountDown, MissionStatement
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.sponsors.models import Sponsor, SponsorshipLevel


def home(request):
    q = Q(conference=request.conference)

    count_down = CountDown.objects.filter(active=True).filter(q)
    keynotes = Speaker.objects.filter(active=True, keynote=True).order_by("full_name").filter(q)

    keystone_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.keystone).filter(q)
    platinum_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.platinum).filter(q)
    gold_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.gold).filter(q)
    silver_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.silver).filter(q)
    partners = Sponsor.objects.filter(level=SponsorshipLevel.partner).filter(q)

    mission_statement = MissionStatement.objects.filter(active=True).filter(q)

    context = {
        "keynotes": keynotes,
        "keystone_sponsors": keystone_sponsors,
        "platinum_sponsors": platinum_sponsors,
        "gold_sponsors": gold_sponsors,
        "silver_sponsors": silver_sponsors,
        "partners": partners,
        "count_down": count_down.first() if count_down else None,
        "mission_statement": mission_statement.first() if mission_statement else None,
        "meta": request.conference.as_meta(),
    }
    return render(request, "home.html", context)
