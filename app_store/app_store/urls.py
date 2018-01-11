from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app_store.views.home', name='home'),
    url(r'^api/$', views.index),
    url(r'^api/app/(?P<app_id>\d+)/(?P<param1>\w+)', views.app),

    url(r'^admin/', include(admin.site.urls)),
)
