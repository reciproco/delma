"""delma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from fichas.admin import admin_site
from fichas.views import FichaIndexView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^delma/', admin_site.urls),
    url(r'^delma/login/$', auth_views.login, name='account_login'),
    url(r'^fichas/', include('fichas.urls')),
    url(r'^seguridad/', include('seguridad.urls')),
    url(r'^$', FichaIndexView.as_view(), name='index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

