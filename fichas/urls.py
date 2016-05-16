from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

from fichas.views import FichaList, FichaDetail, FichaSearchView, download_file

app_name = 'fichas'

urlpatterns = [
    url(r'^$', FichaSearchView.as_view(), name='search'),
    url(r'^media/(?P<name>[\w\.]+)$', download_file),
    url(r'^search/$', FichaList.as_view(), name='ficha-list'),
    url(r'^(?P<pk>[0-9]+)/$', FichaDetail.as_view(), name='ficha-detail'),

]
