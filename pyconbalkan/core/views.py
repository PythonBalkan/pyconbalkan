from django.shortcuts import render

from pyconbalkan.conference.models import Conference, CountDown, MissionStatement
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.sponsors.models import Sponsor, SponsorshipLevel


def home(request):
    conference = Conference.objects.filter(active=True)
    count_down = CountDown.objects.filter(active=True)
    keynotes = Speaker.objects.filter(active=True, keynote=True).order_by('full_name')

    keystone_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.keystone)
    platinum_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.platinum)
    gold_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.gold)
    silver_sponsors = Sponsor.objects.filter(level=SponsorshipLevel.silver)
    partners = Sponsor.objects.filter(level=SponsorshipLevel.partner)

    mission_statement = MissionStatement.objects.filter(active=True)

    context = {
        'keynotes': keynotes,
        'keystone_sponsors': keystone_sponsors,
        'platinum_sponsors': platinum_sponsors,
        'gold_sponsors': gold_sponsors,
        'silver_sponsors': silver_sponsors,
        'partners': partners,
        'count_down': count_down.first() if count_down else None,
        'mission_statement': mission_statement.first() if mission_statement else None,
        'meta': conference.first().as_meta(),
    }
    return render(request, 'home.html', context)


