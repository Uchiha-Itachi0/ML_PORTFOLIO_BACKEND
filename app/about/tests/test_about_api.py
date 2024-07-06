""" Test for about API """

from django.test import TestCase
from django.urls import reverse

from core.models import User, About

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

ABOUT_URL = reverse('about:about')


class PublicAboutAPITest(TestCase):
    """Test for the public about API"""

    def setUp(self):
        self.client = APIClient()
        About.objects.create(content="Test content", skills=["Skill1", "Skill2"], color_text=["#FFFFFF"], colors=["#000000"])

    def test_get_about_successful(self):
        """Test if the about is fetched"""

        res = self.client.get(ABOUT_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class PrivateAboutAPITest(TestCase):
    """Test for authorized User"""

    def setUp(self):
        self.client = APIClient()
        About.objects.create(content="Test content", skills=["Skill1", "Skill2"], color_text=["#FFFFFF"], colors=["#000000"])
        if not User.objects.exists():
            self.user = User.objects.create_user(email='testuser@email.com', password='testpassword')
        else:
            self.user = User.objects.first()

        # Obtain JWT token for authentication
        self.access_token = AccessToken.for_user(self.user)

        # Set authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_update_about_successful(self):

        payload = {
            'content': 'Hello',
            'skills': ['one'],
            'color_text': ['this'],
            'colors': ['that']
        }

        res = self.client.patch(ABOUT_URL, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_about_wrong_skills(self):

        payload = {
            'content': 'Hello',
            'skills': 'one',
            'color_text': ['this'],
            'colors': ['that']
        }

        res = self.client.patch(ABOUT_URL, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_about_wrong_color_text(self):

        payload = {
            'content': 'Hello',
            'skills': 'one',
            'color_text': 'this',
            'colors': ['that']
        }

        res = self.client.patch(ABOUT_URL, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_about_wrong_colors(self):

        payload = {
            'content': 'Hello',
            'skills': 'one',
            'color_text': ['this'],
            'colors': 'that'
        }

        res = self.client.patch(ABOUT_URL, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
