from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import registration
from hitcount.views import update_hit_count_ajax

urlpatterns = patterns('',
#     Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('registration.urls')),
    url(r'^', include('social_auth.urls')),
    url('^', include('flaggit.urls')),
)
