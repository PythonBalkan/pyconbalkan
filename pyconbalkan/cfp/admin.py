from django.contrib import admin
from pyconbalkan.cfp.models import Cfp, CFPRating


class CfpAdmin(admin.ModelAdmin):
    class Meta:
        model = Cfp


class CfpRatingAdmin(admin.ModelAdmin):
    class Meta:
        model = CFPRating


admin.site.register(Cfp, CfpAdmin)
admin.site.register(CFPRating, CfpAdmin)

