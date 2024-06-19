"""
Test for USER API
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
import environ

TOKEN_URL = reverse('user:login')


def create_user(**params):
    """Helper function to create and return new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserAPITest(TestCase):
    """Test the public feature of the user"""

    def setUp(self):
        self.client = APIClient()

    def test_create_token_successful(self):
        """Test Generation of token with valid credential"""
        user_details = {
            'name': 'sakshi',
            'email': 'sakshigopal@example.com',
            'password': 'sakshi1234'
        }

        create_user(**user_details)

        payload = {
            'email': user_details['email'],
            'password': user_details['password']
        }

        res = self.client.post(TOKEN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('access', res.data)
        self.assertIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_bad_credential(self):
        """Test return error if credential is invalid"""

        create_user(email='sakshigopal@example.com', password='sakshi1234')
        payload = {
            'email': 'sakshigopal@example.com',
            'password': 'sakshi'
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_token_blank_password(self):
        """Test posting a blank password raise an error"""

        payload = {
            'email': 'sakshigopal@example.com',
            'password': ''
        }
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('access', res.data)
        self.assertNotIn('refresh', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
