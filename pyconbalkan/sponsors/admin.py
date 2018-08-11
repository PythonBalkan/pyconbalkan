from django.contrib import admin
from pyconbalkan.sponsors.models import Package, PackageItem, Sponsor, Sponsoring

admin.site.register(Sponsor)
admin.site.register(Sponsoring)
admin.site.register(Package)
admin.site.register(PackageItem)
