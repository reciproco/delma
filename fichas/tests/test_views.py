from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from fichas.models import Ficha
from django.utils import timezone
from model_mommy import mommy

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'prueba')
        self.client.login(username='test', password='prueba')
        self.ficha = mommy.make(Ficha)

    def test_search(self):
        response = self.client.get(reverse('fichas:search'))
        self.assertEqual(response.status_code, 200)

    def test_media(self):
        response = self.client.get(reverse('fichas:media', kwargs={'name':'peloto.jpg'}))
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
