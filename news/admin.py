from django.contrib import admin

from .models import News, NewsImage


class NewsImageAdmin(admin.StackedInline):
    model = NewsImage


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin]

    class Meta:
        model = News


@admin.register(NewsImage)
class NewImageAdmin(admin.ModelAdmin):
    pass
