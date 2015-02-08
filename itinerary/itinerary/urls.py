from django.conf.urls import patterns, include, url
from django.contrib import admin
import itineraryapp.views

urlpatterns = patterns('',
    url(r'^$', itineraryapp.views.home, name='home'),
    url(r'^home.html$', itineraryapp.views.home, name='home'),
    url(r'^mongonaut/', include('mongonaut.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
)