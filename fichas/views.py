from django.shortcuts import render

# Create your views here.
import  logging
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q
from fichas.models import Ficha

class FichaList(ListView):
    model = Ficha

    def get_queryset(self):
        qs = super(FichaList, self).get_queryset()
        nombre = self.request.GET.get('nombre')
        if nombre:
            logging.error("AQUIIIIII")
            #return qs.filter(paciente__apellido1__icontains=nombre)
            return qs.filter(Q(paciente__apellido1__icontains=nombre) | Q(paciente__nombre__icontains=nombre))
        return qs

class FichaDetail(DetailView):
    model = Ficha

class FichaIndexView(TemplateView):
    template_name = 'fichas/index.html'
