from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agent.views.home', name='home'),
    url(r'^versity/', include('versity.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
