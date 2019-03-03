from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from pyconbalkan.conference.abstractions import ConferenceAbstractAdmin
from pyconbalkan.news.models import Post


class PostAdmin(ConferenceAbstractAdmin, MarkdownxModelAdmin):
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
