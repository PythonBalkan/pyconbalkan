from django_seed import Seed
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyconbalkan.settings")
django.setup()
seeder = Seed.seeder()

from pyconbalkan.conference.models import Conference

seeder.add_entity(Conference, 5)


inserted_pks = seeder.execute()
