from django.test import TestCase
from django.test import Client

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_auth_base_endpoint(self):
        response = self.client.get('/fichas/')
        self.assertEqual(response.status_code, 302)

    def test_auth_list_endpoint(self):
        response = self.client.get('/fichas/search/?nombre=')
        self.assertEqual(response.status_code, 302)

    def test_auth_detail_endpoint(self):
        response = self.client.get('/fichas/1/')
        self.assertEqual(response.status_code, 302)

    def test_auth_detail_endpoint(self):
        response = self.client.get('/fichas/media/133de48794304b15973f4a2522987698.JPG')
        self.assertEqual(response.status_code, 302)


