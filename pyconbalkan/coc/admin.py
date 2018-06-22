from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import CodeOfConduct, ResponseGuide


class CodeOfConductAdmin(MarkdownxModelAdmin):
    class Meta:
        model = CodeOfConduct


class ResponseGuideAdmin(MarkdownxModelAdmin):
    class Meta:
        model = ResponseGuide


admin.site.register(CodeOfConduct, CodeOfConductAdmin)
admin.site.register(ResponseGuide, ResponseGuideAdmin)
