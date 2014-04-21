from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'eventos.views.home', name='home'),
    url(r'^(?P<evento>[0-9]+)$', 'eventos.views.home', name='home2'),
    url(r'^novo$' , 'eventos.views.ve', name='novo'),
    url(r'^meus$', 'eventos.views.meus_buracos', name='meus'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static('/media/', document_root=settings.MEDIA_ROOT)
