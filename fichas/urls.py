from django.conf.urls import url

from . import views

from fichas.views import FichaList, FichaDetail, FichaIndexView

app_name = 'fichas'

urlpatterns = [
    url(r'^$', FichaIndexView.as_view(), name='index'),
#    url(r'^search/(?P<pk>[0-9]+)/$', FichaList.as_view()),
    url(r'^search/$', FichaList.as_view(), name='ficha-list'),
    url(r'^(?P<pk>[0-9]+)/$', FichaDetail.as_view(), name='ficha-detail'),
]
