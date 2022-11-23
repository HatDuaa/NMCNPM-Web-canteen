from urllib import response
from django.test import TestCase, SimpleTestCase

# Create your tests here.
class simpleTests(SimpleTestCase):
    def test_home_app_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
