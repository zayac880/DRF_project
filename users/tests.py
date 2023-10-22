from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from users.models import User


class UserRegistrationTestCase(APITestCase):
    def test_user_registration(self):
        data = {
            'email': 'testuser@example.com',
            'password': 'testpassword',
        }

        url = reverse('users:user-list-create')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email=data['email']).exists())
