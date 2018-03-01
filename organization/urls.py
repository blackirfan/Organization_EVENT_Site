from django.conf.urls import url
from . import views

app_name = 'organization'

urlpatterns = [

# this is most common url pattern index which go to home area
    url(r'^$', views.index, name='index'),
    # when url connect with start like 8000/organization/start
    #  then it response with view.py class name start
    url(r'^start$', views.start, name='start'),

    # this is also same way work how a start is work their
    url(r'^about/$', views.about, name='about'),
    # this is work on register work in user 
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<organization_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<special_event_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^special_events/(?P<filter_by>[a-zA_Z]+)/$', views.special_events, name='special_events'),
       # (?P<organization_id>[0-9]+ this is actually work a unique user id on their which is
       #  represent any 0-9 number
    url(r'^create_organization/$', views.create_organization, name='create_organization'),
    url(r'^(?P<organization_id>[0-9]+)/create_special_event/$', views.create_special_event, name='create_special_event'),
    url(r'^(?P<organization_id>[0-9]+)/delete_special_event/(?P<special_event_id>[0-9]+)/$', views.delete_special_event, name='delete_special_event'),
    url(r'^(?P<organization_id>[0-9]+)/favorite_organization/$', views.favorite_organization, name='favorite_organization'),
    url(r'^(?P<organization_id>[0-9]+)/delete_organization/$', views.delete_organization, name='delete_organization'),
    url(r'^(?P<organization_id>[0-9]+)/event_detail/$', views.event_detail, name='event_detail'),


]
