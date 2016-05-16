from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

# Register your models here.
from django.contrib.admin import AdminSite

from .models import Paciente, Ficha, Adjunto

class AdjuntoInline(admin.StackedInline):
    extra = 0
    model = Adjunto

class FichaAdmin(admin.ModelAdmin):
    inlines = [
        AdjuntoInline,
    ]
    list_display = ('paciente','lesion','observaciones', 'adjuntos','cuando')
    search_fields = ('paciente__nombre','lesion')
    ordering = ('-cuando',)

    def adjuntos(self, obj):
        html=''
        for c in obj.adjunto_set.order_by('nombre'):
            html = html + '<a href="{}">{}</a><br/>'.format(c.fichero.url,c.nombre)
        return html
        #return '<br/>'.join(c.nombre for c in obj.adjunto_set.order_by('nombre'))
    adjuntos.allow_tags = True

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo','telefono', 'correo', 'alta')
    search_fields = ('nombre_completo','telefono','correo')
    ordering = ('-alta',)

class MyAdminSite(AdminSite):
    site_header = 'DELMA Administrador'

admin_site = MyAdminSite(name='delma')

# Register your models here.
admin_site.register(Paciente, PacienteAdmin)
admin_site.register(Ficha, FichaAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)

