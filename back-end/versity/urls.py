from django.conf.urls import patterns, include, url
from .views import (us,newss,full_scholar,partial_scholar,bac_view,mas_view,phd_view)


urlpatterns = patterns('',
     url(r'^us/$',us ),
     url(r'^news/$',newss ),
     url(r'^full_scholar/$',full_scholar),
     url(r'^partial_scholar/$',partial_scholar),
     url(r'^bac/$',bac_view),
     url(r'^mas/$',mas_view),
     url(r'^phd/$',phd_view),


)
