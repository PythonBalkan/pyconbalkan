from django.contrib import admin

from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    class Meta:
        model = Faq


admin.site.register(Faq, FaqAdmin)

