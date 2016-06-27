from django.shortcuts import render
from django.conf import settings
import os, mimetypes

# Create your views here.
import  logging
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from fichas.models import Ficha
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required(login_url='/seguridad/login/')
def download_file(request, name):
    mimetype = mimetypes.guess_type(os.path.join(settings.MEDIA_ROOT,name))
    with open(os.path.join(settings.MEDIA_ROOT,name), 'rb') as f:
         
        response = HttpResponse(f, content_type = mimetype)
        response['Content-Disposition'] = "attachment; filename=%s" % \
                                     (name)
        return response

        
class FichaList(LoginRequiredMixin,ListView):
    model = Ficha
    login_url = '/seguridad/login/'

    def get_queryset(self):
        qs = super(FichaList, self).get_queryset()
        nombre = self.request.GET.get('nombre')
        if nombre:
            logging.error("AQUIIIIII")
            #return qs.filter(paciente__apellido1__icontains=nombre)
            return qs.filter(Q(paciente__apellido1__icontains=nombre) | Q(paciente__nombre__icontains=nombre))
        return qs

class FichaDetail(LoginRequiredMixin,DetailView):
    login_url = '/seguridad/login/'
    model = Ficha

class FichaIndexView(LoginRequiredMixin,TemplateView):
    login_url = '/seguridad/login/'
    template_name = 'fichas/index.html'

class FichaSearchView(LoginRequiredMixin,TemplateView):
    login_url = '/seguridad/login/'
    template_name = 'fichas/search.html'
