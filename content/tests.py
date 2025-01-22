from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Content
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class ContentTests(APITestCase):
     def setUp(self):
         self.author = User.objects.create_user(
            email='author@example.com',
            password='AuthorPassword123',
            first_name='Author',
            last_name='User',
            phone='1234567890'
         )
         self.admin = User.objects.create_superuser(
            email='admin@example.com',
            password='AdminPassword123',
            first_name='Admin',
            last_name='User',
            phone='1234567890'
         )
         refresh = RefreshToken.for_user(self.author)
         self.author_token = str(refresh.access_token)
         refresh_admin = RefreshToken.for_user(self.admin)
         self.admin_token = str(refresh_admin.access_token)

     def test_author_create_content(self):
        url = reverse('author-content-list-create')
        data = {
            'title': 'Test Title',
            'body': 'Test body content. This is a sample',
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.author_token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Content.objects.count(), 1)
        content = Content.objects.first()
        self.assertEqual(content.author, self.author)

     def test_author_cannot_create_content_without_token(self):
         url = reverse('author-content-list-create')
         data = {
             'title': 'Test Title',
             'body': 'Test body content. This is a sample',
         }
         response = self.client.post(url, data, format='json')
         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
     
     def test_admin_can_create_content(self):
         url = reverse('admin-content-list-create')
         data = {
             'title': 'Admin Test Title',
             'body': 'Admin Test body content. This is a sample',
             'author': self.admin.id
         }
         self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
         response = self.client.post(url, data, format='json')
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
         self.assertEqual(Content.objects.count(), 1)
         content = Content.objects.first()
         self.assertEqual(content.author, self.admin)

     def test_author_cannot_create_content_using_admin_view(self):
        url = reverse('admin-content-list-create')
        data = {
            'title': 'Test Title',
            'body': 'Test body content. This is a sample',
            'author': self.author.id
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.author_token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)