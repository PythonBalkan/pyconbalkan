from datetime import datetime

import requests
from django.core.management.base import BaseCommand
from django.db.models import Prefetch
from django.utils import timezone
from fuzzyfinder.main import fuzzyfinder

from pyconbalkan.conference.models import Conference
from pyconbalkan.speaker.models import Speaker
from pyconbalkan.timetable.models import Presentation, Room, Slot

from django.core.exceptions import ObjectDoesNotExist

ALL_DATA_URL = "https://sessionize.com/api/v2/fwv5aino/view/All"


class Command(BaseCommand):
    help = 'Import data from sessionize'

    def add_arguments(self, parser):
        pass
        parser.add_argument('--year', nargs="?", type=int, default=timezone.now().year)
        parser.add_argument('--force', action="store_true")
        parser.add_argument('--data_url', nargs="?", type=str, default=ALL_DATA_URL)

    def handle(self, *args, **options):
        conference = Conference.objects.get(year=options['year'])
        _cant_find = []

        data = requests.get(options['data_url']).json()

        questions = data['questions']
        categories = data['categories']
        rooms = data['rooms']
        sessions = data['sessions']
        speakers = data['speakers']

        types = categories[0]['items']
        types = {x['id']:x['name'] for x in types}

        Presentation.objects.filter(conference=conference).delete()
        Room.objects.filter(conference=conference).delete()
        Slot.objects.filter(conference=conference).delete()

        for room in rooms:
            Room.objects.get_or_create(
                pk=room['id'],
                conference=conference,
                name=room['name'],
                sort_order=room['sort']
            )


        for session in sessions:
            speaker_id = session['speakers'][0]
            speaker = self.get_speaker(speaker_id, speakers)

            if speaker == None:
                print(speaker_id, 'Not found')
            else:
                speaker = speaker.id

            presentation, created = Presentation.objects.get_or_create(
                pk=session['id'],
                active=False,
                title=session['title'],
                description=session['description'],
                type=Presentation.PRESENTATION_TYPE_REVERSE[types[session['categoryItems'][0]]],
                speaker_id=speaker,
                conference_id=conference.id,
            )

            start = timezone.make_aware(datetime.strptime(session['startsAt'], "%Y-%m-%dT%H:%M:%S"))
            end = timezone.make_aware(datetime.strptime(session['endsAt'], "%Y-%m-%dT%H:%M:%S"))
            Slot.objects.get_or_create(
                active=False,
                from_date=start,
                to_date=end,
                room_id=session['roomId'],
                talk_id=presentation.id,
                conference_id=conference.id,
            )

        if any(_cant_find):
            if options['force']:
                print(_cant_find)
            else:
                raise Exception("Had problems with the following", _cant_find)

    def get_speaker(self, speaker_id, speakers):
        for speaker in speakers:
            if speaker['id'] == speaker_id:
                full_name = " ".join(speaker['fullName'].split())
                try:
                    return Speaker.objects.get(full_name=full_name)
                except ObjectDoesNotExist:
                    return None
        return None