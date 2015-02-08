from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

import itineraryapp.views

urlpatterns = patterns('',
    url(r'^$', itineraryapp.views.home, name='home'),
    url(r'^home.html$', itineraryapp.views.home, name='home'),
    url(r'^mytrip.html$', itineraryapp.views.get_itinerary, name='get_itinerary'),
    url(r'^mongonaut/', include('mongonaut.urls')),
    url(r'^admin/', include(admin.site.urls)),   
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
