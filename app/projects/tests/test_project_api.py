"""Test for the project API"""

from django.test import TestCase
from django.urls import reverse
from core.models import Project, User

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken


class PublicProjectAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_fetch_successful(self):
        """Test for getting the data successfully"""
        url = reverse('project:get-no-query')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_project_unauthorized(self):
        """Test if creating a project is unauthorized"""

        payload = {
            'tags': ['Python', 'ML'],
            'time': '20 April 2024',
            'title': 'Test Project',
            'subtitle': 'Subtitle',
            'link': 'https://www.example.com'
        }
        url = reverse('project:get-no-query')
        res = self.client.post(url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_unauthorized(self):
        """Test unauthorized user can't update the data"""
        payload = Project.objects.create(tags=['Python', 'React'], time='20 April 2024', title='Test Blog',
                                         subtitle='Subtitle',
                                         link='https://www.example.com')

        updated_payload = {
            'tags': ['Python', 'Java'],
            'time': '21 April 2024',
            'title': 'Updated_payload',
            'subtitle': 'Updated subtitle',
            'link': 'https://www.example.com'
        }
        url = reverse('project:get-query', args=[payload.id])
        res = self.client.patch(url, updated_payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_project_unauthorized(self):
        """Test if deleting a project is unauthorized"""

        blog = Project.objects.create(tags=['React', 'Nextjs'], time='20 April 2024', title='Test Blog',
                                      subtitle='Subtitle',
                                      link='https://www.example.com')

        url = reverse('project:get-query', args=[blog.id])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateProjectAPITest(TestCase):
    """Test for the Project API with authentication"""

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

    def test_create_project_wrong_tags_type(self):
        """Test creating project with wrong tags type"""
        payload = {
            'tags': 'Python',
            'time': '20 April 2024',
            'title': 'Test Project',
            'subtitle': 'Subtitle',
            'link': 'https://www.example.com'
        }

        url = reverse('project:get-no-query')
        res = self.client.post(url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_project_successful(self):
        """Test if creating a project is successful"""

        payload = {
            'tags': ['Python', 'ML'],
            'time': '20 April 2024',
            'title': 'Test Project',
            'subtitle': 'Subtitle',
            'link': 'https://www.example.com'
        }

        url = reverse('project:get-no-query')
        res = self.client.post(url, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_project_successful(self):
        """Test if updating a project is successful"""

        payload = Project.objects.create(tags=['Python', 'C++'], time='20 April 2024', title='Test Blog',
                                         subtitle='Subtitle',
                                         link='https://www.example.com')

        updated_payload = {
            'tags': ['Python', 'C++'],
            'time': '21 April 2024',
            'title': 'Updated Test Project',
            'subtitle': 'Updated Subtitle',
            'link': 'https://www.updated-example.com'
        }

        url = reverse('project:get-query', args=[payload.id])
        res = self.client.put(url, updated_payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_blog_successful(self):
        """Test if deleting a blog is successful"""

        payload = Project.objects.create(time='20 April 2024', title='Test Blog', subtitle='Subtitle',
                                         link='https://www.example.com')

        url = reverse('project:get-query', args=[payload.id])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
