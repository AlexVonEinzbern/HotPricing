from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class RegisterTestCase(TestCase):
    def test_register(self):
        response = self.client.post('/api/register/', {
            'username': 'testuser',
            'email': 'testuser@testmail.com',
            'password': 'testpass',
        })
        self.assertEqual(response.status_code, 200)

class LoginTestCase(TestCase):
    def test_login(self):
        # Registration
        register_response = self.client.post('/api/register/', {
            'username': 'testuser',
            'email': 'testuser@testmail.com',
            'password': 'testpass',
        })

        # Login
        login_response = self.client.post('/api/login/', {
            'username': 'testuser',
            'password': 'testpass',
        })
       
        self.assertEqual(login_response.status_code, 200)