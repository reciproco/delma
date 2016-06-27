from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from fichas import models
from django.utils import timezone

class ViewsTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'prueba')
        self.client.login(username='test', password='prueba')
        self.paciente = models.Paciente.objects.create(nombre='prueba',apellido1='p',apellido2='p',direccion='calle',telefono='917732443',correo='a@test.com',dni='50867534W',nacimiento=timezone.now(), alta=timezone.now())
        self.ficha = models.Ficha.objects.create(paciente=self.paciente,lesion='pupa',cuando=timezone.now(), como='caida', observaciones='aa', dolor='mucho', sesiones= 3)

    def test_search(self):
        response = self.client.get(reverse('fichas:search'))
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = self.client.get(reverse('fichas:ficha-list'))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(reverse('fichas:ficha-detail', kwargs={'pk':self.ficha.pk}))
        self.assertEqual(response.status_code, 200)

    def test_detail_404(self):
        response = self.client.get(reverse('fichas:ficha-detail', kwargs={'pk':40}))
        self.assertEqual(response.status_code, 404)
