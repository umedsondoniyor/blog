from django.conf.urls import url
from .views import *

app_name = 'post'

urlpatterns = [

    url(r'^index/$', post_index, name='index'),

    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),      # d+ regular expressions means that it can include many digits

    url(r'^create/$', post_create, name='create'),

    url(r'^(?P<id>\d+)/update/$', post_update, name='update'),

    url(r'^(?P<id>\d+)/delete/$', post_delete, name='delete'),
]