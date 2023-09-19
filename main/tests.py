from django.test import TestCase
from main.models import Product

class MainTest(TestCase):

    def test_main_url_is_exist(self):
        response = self.client.get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('/main/')
        self.assertTemplateUsed(response, 'main.html')