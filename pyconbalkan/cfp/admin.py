from django.contrib import admin

from pyconbalkan.cfp.models import Cfp, CFPRating


@admin.register(Cfp)
class CfpAdmin(admin.ModelAdmin):
    list_filter = (
        "conference__year",
        "active"
    )
    autocomplete_fields = ("speaker",)
    list_display = ("name", "title", "speaker", "duration", "active",)
    list_editable = ("active",)


admin.site.register(CFPRating)
