from django.db.models import Q
from django.shortcuts import render

from pyconbalkan.conference.models import CountDown, MissionStatement
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.sponsors.models import Sponsor, SponsorshipLevel
from pyconbalkan.timetable.models import Presentation


def home(request):
    count_down = CountDown.objects.filter(active=True)
    keynotes = Speaker.objects.filter(
        presentations__active=True,
        presentations__type=Presentation.KEYNOTE,
        presentations__conference__active=True
    ).order_by("full_name")

    keystone_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.keystone, active=True, conference__active=True)
    platinum_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.platinum, active=True, conference__active=True)
    gold_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.gold, active=True, conference__active=True)
    silver_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.silver, active=True, conference__active=True)
    partners = Sponsor.objects.filter(level=SponsorshipLevel.partner, active=True)

    mission_statement = MissionStatement.objects.filter(active=True)

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
