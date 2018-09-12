from django.conf import settings
from django.conf.urls import url

from . import views

app_name = 'borrel'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<item_id>[0-9]+)/result/$', views.result, name='result'),
]