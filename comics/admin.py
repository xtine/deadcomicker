from comics.models import Comic
from django.contrib import admin

class ComicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ['title']

admin.site.register(Comic, ComicAdmin)
