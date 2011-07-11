from comics.models import Comic
from django.contrib import admin

class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

admin.site.register(Comic, ComicAdmin)
