from django.test import TestCase, Client
from django.urls import reverse
from .models import *

class TestViews(TestCase):

    def test_markets(self):
        client = Client()

        response = client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    