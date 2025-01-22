from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserRegistrationTests(APITestCase):

    def test_register_valid_user(self):
        url = reverse('user-registration')
        data = {
            'email': 'test@example.com',
            'password': 'TestPassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@example.com')

    def test_register_invalid_email(self):
        url = reverse('user-registration')
        data = {
            'email': 'invalid_email',
            'password': 'TestPassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_password_length(self):
        url = reverse('user-registration')
        data = {
            'email': 'test@example.com',
            'password': 'Test1',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_password_no_uppercase(self):
        url = reverse('user-registration')
        data = {
            'email': 'test@example.com',
            'password': 'testpassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_password_no_lowercase(self):
        url = reverse('user-registration')
        data = {
            'email': 'test@example.com',
            'password': 'TESTPASSWORD123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '1234567890'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_invalid_phone(self):
        url = reverse('user-registration')
        data = {
            'email': 'test@example.com',
            'password': 'TestPassword123',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '123456'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UserLoginTests(APITestCase):
    def setUp(self):
         self.user = User.objects.create_user(
            email='test@example.com',
            password='TestPassword123',
            first_name='Test',
            last_name='User',
            phone='1234567890'
         )

    def test_login_valid_user(self):
        url = reverse('user-login')
        data = {
          'email': 'test@example.com',
          'password': 'TestPassword123'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_user(self):
        url = reverse('user-login')
        data = {
            'email': 'invalid@example.com',
            'password': 'InvalidPassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_invalid_password(self):
        url = reverse('user-login')
        data = {
            'email': 'test@example.com',
            'password': 'InvalidPassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)