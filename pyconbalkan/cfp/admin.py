from django.contrib import admin

from pyconbalkan.cfp.models import Cfp, CFPRating


@admin.register(Cfp)
class CfpAdmin(admin.ModelAdmin):
    list_filter = (
        "conference__name",
    )


admin.site.register(CFPRating)
