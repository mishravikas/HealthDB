from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'HealthDB.views.hello',),
    # url(r'^patient/', include('HealthDB.patient.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
