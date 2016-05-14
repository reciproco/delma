from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'seguridad'

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
