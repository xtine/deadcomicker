from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),    
    (r'^grappelli/', include('grappelli.urls')),
    (r'^$', 'comics.views.index'),
)

if settings.LOCAL_MEDIA:
    urlpatterns +=patterns('',
        (r'^static/(.+)', 'django.views.static.serve', { 'document_root' : settings.STATIC_ROOT }),
        (r'^media/(.+)', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT })
    )