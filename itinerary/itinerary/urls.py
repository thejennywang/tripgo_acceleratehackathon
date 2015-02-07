from django.conf.urls import patterns, include, url
from django.contrib import admin
import itineraryapp

urlpatterns = patterns('',
    url(r'^$', itineraryapp.views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
