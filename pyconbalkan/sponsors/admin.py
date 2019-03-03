from django.contrib import admin

from pyconbalkan.conference.abstractions import ConferenceAbstractAdmin
from pyconbalkan.sponsors.models import Package, PackageItem, Sponsor, Sponsoring


admin.site.register(Sponsor, ConferenceAbstractAdmin)
admin.site.register(Sponsoring)
admin.site.register(Package)
admin.site.register(PackageItem)
