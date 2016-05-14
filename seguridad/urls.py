from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'seguridad'

urlpatterns = [
    url(r'^login/$', auth_views.login,{'template_name': 'seguridad/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'seguridad/logout.html'}, name='logout'),
]
