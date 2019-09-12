from datetime import datetime

import requests
from django.core.management.base import BaseCommand
from django.db.models import Prefetch
from django.utils import timezone
from fuzzyfinder.main import fuzzyfinder

from pyconbalkan.conference.models import Conference
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.timetable.models import Presentation, Room, Slot

ALL_DATA_URL = "https://sessionize.com/api/v2/fwv5aino/view/All"


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass
        parser.add_argument('--year', nargs="?", type=int, default=timezone.now().year)
        parser.add_argument('--force', action="store_true")
        parser.add_argument('--data_url', nargs="?", type=str, default=ALL_DATA_URL)

    def handle(self, *args, **options):
        conference = Conference.objects.get(year=options['year'])

        data = requests.get(options['data_url']).json()

        questions = data['questions']
        categories = data['categories']
        rooms = data['rooms']

        # Sync rooms
        Room.objects.filter(conference=conference).delete()
        Slot.objects.filter(conference=conference).delete()
        all_presentations_this_year = list(Presentation.objects.filter(conference=conference).values_list("id", "title"))

        for room in rooms:
            Room.objects.create(
                pk=room['id'],
                conference=conference,
                name=room['name'],
                sort_order=room['sort']
            )


        # Make speaker dict
        speakers = {}
        for _ in data['speakers']:
            first_name = _.pop('firstName')
            last_name = _.pop('lastName')
            speakers[f"{first_name} {last_name}"] = _

        for speaker in speakers.values():
            for i, session in enumerate(speaker['sessions']):
                speaker['sessions'][i] = list(filter(lambda _: int(_['id']) == session, data['sessions']))[0]

        #  Attach Speaker obj from DB
        speakers_qs = Speaker.objects.all().prefetch_related(
            Prefetch(
                "presentations",
                queryset=Presentation.objects.filter(active=True, conference=conference).order_by("type")
            )
        )

        _cant_find = []
        for speaker in speakers_qs:
            if not any(speaker.presentations.all()):
                continue

            r = list(fuzzyfinder(speaker.full_name, speakers.keys()))
            if not any(r):
                _cant_find.append(speaker)
                continue
            speakers[r[0]]["model_speaker"] = speaker
            speaker = speakers[r[0]]

            for _ in speaker['sessions']:
                r = list(fuzzyfinder(_['title'], list(zip(*all_presentations_this_year))[1]))
                if not any(r):
                    _cant_find.append(_)


                try:
                    presentation = Presentation.objects.get(title__icontains=_['title'])
                except Presentation.DoesNotExist:
                    _cant_find.append(_)
                # TODO NEXT YEAR MAYBE, GET TZ FROM CONFERENCE OBJECT ?!
                Slot.objects.create(
                    from_date=timezone.make_aware(datetime.strptime(_['startsAt'], "%Y-%m-%dT%H:%M:%S")),
                    to_date=timezone.make_aware(datetime.strptime(_['endsAt'], "%Y-%m-%dT%H:%M:%S")),
                    talk=presentation,
                    room=Room.objects.get(pk=_['roomId']),
                    conference=conference
                )

        if any(_cant_find):
            if options['force']:
                print(_cant_find)
            else:
                raise Exception("Had problems with the following", _cant_find)
