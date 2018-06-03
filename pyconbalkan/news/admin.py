from django.contrib import admin

from pyconbalkan.news.models import Post


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
