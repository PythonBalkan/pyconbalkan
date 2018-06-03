from django.contrib import admin
from pyconbalkan.sponsors.models import Sponsor, PackageOption, SponsorshipPackage

admin.site.register(Sponsor)
admin.site.register(SponsorshipPackage)
admin.site.register(PackageOption)
