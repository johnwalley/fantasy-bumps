from django.conf.urls import url

from . import views

app_name = 'fantasybumps'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^crew/(?P<crew_id>[0-9]+)/$', views.crew_detail, name='crew_detail'),
    url(r'^rower/(?P<rower_id>[0-9]+)/$', views.rower_detail, name='rower_detail'),
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.profile_detail, name='profile_detail'),
    url(r'^table/$', views.table, name="table"),
]
