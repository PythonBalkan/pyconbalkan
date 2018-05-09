from django.contrib import admin

from .models import About


class AboutAdmin(admin.ModelAdmin):
    class Meta:
        model = About

admin.site.register(About, AboutAdmin)
