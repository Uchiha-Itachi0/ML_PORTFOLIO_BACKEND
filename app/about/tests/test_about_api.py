""" Test for about API """

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

ABOUT_URL = reverse('about:get')


ADMIN_ABOUT_URL = reverse('about:get_admin')


class AboutAPITest(TestCase):
    """Test for the public about API"""

    def setUp(self):
        self.client = APIClient()

    def test_get_about_successful(self):
        """Test if the about is fetched"""

        res = self.client.get(ABOUT_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_admin_about_unsuccessful(self):
        """Test if the admin about is not fetched"""

        res = self.client.get(ADMIN_ABOUT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
