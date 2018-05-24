from django.contrib import admin
from pyconbalkan.cfp.models import Cfp


class CfpAdmin(admin.ModelAdmin):
    class Meta:
        model = Cfp


admin.site.register(Cfp, CfpAdmin)

