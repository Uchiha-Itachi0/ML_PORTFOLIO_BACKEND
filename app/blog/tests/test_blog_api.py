# tests/test_blog_api.py
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from core.models import Blogs, User
from rest_framework_simplejwt.tokens import AccessToken

BLOG_URL = reverse('blog:get')
# ADMIN_BLOG_URL = reverse('blog:get_admin')


class PublicBlogAPITest(TestCase):
    """Test for the Blog API without authentication"""

    def setUp(self):
        self.client = APIClient()

    def test_get_blogs_successful(self):
        """Test if blogs are fetched successfully"""

        res = self.client.get(BLOG_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_blog_unauthorized(self):
        """Test if creating a blog is unauthorized"""

        payload = {
            'time': '20 April 2024',
            'title': 'Test Blog',
            'subtitle': 'Subtitle',
            'link': 'https://www.example.com'
        }
        url = reverse('blog:create')
        res = self.client.post(url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_blog_unauthorized(self):
        """Test if updating a blog is unauthorized"""

        blog = Blogs.objects.create(time='20 April 2024', title='Test Blog', subtitle='Subtitle',
                                   link='https://www.example.com')

        updated_payload = {
            'time': '21 April 2024',
            'title': 'Updated Test Blog',
            'subtitle': 'Updated Subtitle',
            'link': 'https://www.updated-example.com'
        }

        url = reverse('blog:update', args=[blog.id])
        res = self.client.put(url, updated_payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_blog_unauthorized(self):
        """Test if deleting a blog is unauthorized"""

        blog = Blogs.objects.create(time='20 April 2024', title='Test Blog', subtitle='Subtitle',
                                   link='https://www.example.com')

        url = reverse('blog:delete', args=[blog.id])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateBlogAPITest(TestCase):
    """Test for the Blog API with authentication"""

    def setUp(self):
        self.client = APIClient()
        if not User.objects.exists():
            self.user = User.objects.create_user(email='testuser@email.com', password='testpassword')
        else:
            self.user = User.objects.first()

        # Obtain JWT token for authentication
        self.access_token = AccessToken.for_user(self.user)

        # Set authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_blog_successful(self):
        """Test if creating a blog is successful"""

        payload = {
            'time': '20 April 2024',
            'title': 'Test Blog',
            'subtitle': 'Subtitle',
            'link': 'https://www.example.com'
        }

        url = reverse('blog:create')
        res = self.client.post(url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_blog_successful(self):
        """Test if updating a blog is successful"""

        blog = Blogs.objects.create(time='20 April 2024', title='Test Blog', subtitle='Subtitle',
                                   link='https://www.example.com')

        updated_payload = {
            'time': '21 April 2024',
            'title': 'Updated Test Blog',
            'subtitle': 'Updated Subtitle',
            'link': 'https://www.updated-example.com'
        }

        url = reverse('blog:update', args=[blog.id])
        res = self.client.put(url, updated_payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_blog_successful(self):
        """Test if deleting a blog is successful"""

        blog = Blogs.objects.create(time='20 April 2024', title='Test Blog', subtitle='Subtitle',
                                   link='https://www.example.com')

        url = reverse('blog:delete', args=[blog.id])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
