from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import About


class AboutAdmin(MarkdownxModelAdmin):
    class Meta:
        model = About

admin.site.register(About, AboutAdmin)
