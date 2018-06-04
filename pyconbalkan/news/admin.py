from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from pyconbalkan.news.models import Post


class PostAdmin(MarkdownxModelAdmin):
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
