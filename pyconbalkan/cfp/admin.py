from django.contrib import admin

from pyconbalkan.cfp.models import Cfp, CFPRating


@admin.register(Cfp)
class CfpAdmin(admin.ModelAdmin):
    list_filter = (
        "conference__year",
        "active"
    )
    autocomplete_fields = ("speaker",)


admin.site.register(CFPRating)
