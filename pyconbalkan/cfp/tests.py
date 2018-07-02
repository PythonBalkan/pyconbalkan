from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Cfp, TALK

CFP_URL = '/api/cfp/'


class CfpAuthApiTest(APITestCase):
    """Test that cfp service endpoint permissions are setup correctly."""

    def setUp(self):
        # Create CFP
        self.cfp = Cfp.objects.create(
            name='test',
            email='test@test.com',
            title='Test',
            duration='30min',
            description='Test',
            type=TALK
        )

        # Create user
        self.user = User.objects.create_superuser(username='test', password='1234', email='admin@test.com')

    def test_list_returns_error_for_unauthenticated_user(self):
        """Test that unauthenticated user can't use CFP API endpoint."""

        result = self.client.get(CFP_URL)
        self.assertEqual(status.HTTP_403_FORBIDDEN, result.status_code, 'Status code should be 403 for list.')

    def test_create_returns_error_for_unauthenticated_user(self):
        """Test that unauthenticated user can't use CFP API endpoint."""

        result = self.client.post(CFP_URL, {
            'name': 'test1',
            'email': 'test1@test.com',
            'title': 'Test1',
            'duration': 'Test1',
            'description': 'Test',
            'type': TALK,
        })
        self.assertEqual(status.HTTP_403_FORBIDDEN, result.status_code, 'Status code should be 403 for list.')

    def test_details_returns_error_for_unauthenticated_user(self):
        """Test that unauthenticated user can't use CFP API endpoint."""

        result = self.client.get(CFP_URL + '{}/'.format(self.cfp.id))
        self.assertEqual(status.HTTP_403_FORBIDDEN, result.status_code, 'Status code should be 403 for list.')

    def test_update_returns_error_for_unauthenticated_user(self):
        """Test that unauthenticated user can't use CFP API endpoint."""

        result = self.client.patch(CFP_URL + '{}/'.format(self.cfp.id))
        self.assertEqual(status.HTTP_403_FORBIDDEN, result.status_code, 'Status code should be 403 for list.')

    def test_delete_returns_error_for_unauthenticated_user(self):
        """Test that unauthenticated user can't use CFP API endpoint."""

        result = self.client.delete(CFP_URL + '{}/'.format(self.cfp.id))
        self.assertEqual(status.HTTP_403_FORBIDDEN, result.status_code, 'Status code should be 403 for list.')

    def test_list_returns_success_for_unauthenticated_user(self):
        """Test that authenticated user can use CFP API endpoint."""
        self.client.force_login(self.user)

        result = self.client.get(CFP_URL)
        self.assertEqual(status.HTTP_200_OK, result.status_code, 'Status code should be 200 for list.')

    def test_create_returns_success_for_authenticated_user(self):
        """Test that authenticated user can use CFP API endpoint."""
        self.client.force_login(self.user)

        result = self.client.post(CFP_URL, {
            'name': 'test1',
            'email': 'test1@test.com',
            'title': 'Test1',
            'duration': 'Test1',
            'description': 'Test',
            'type': TALK,
        })
        self.assertEqual(status.HTTP_201_CREATED, result.status_code, 'Status code should be 201 for create.')

    def test_details_returns_success_for_authenticated_user(self):
        """Test that authenticated user can use CFP API endpoint."""
        self.client.force_login(self.user)

        result = self.client.get(CFP_URL + '{}/'.format(self.cfp.id))
        self.assertEqual(status.HTTP_200_OK, result.status_code, 'Status code should be 200 for details.')

    def test_update_returns_success_for_authenticated_user(self):
        """Test that authenticated user can use CFP API endpoint."""
        self.client.force_login(self.user)

        result = self.client.patch(CFP_URL + '{}/'.format(self.cfp.id))
        self.assertEqual(status.HTTP_200_OK, result.status_code, 'Status code should be 200 for update.')

    def test_delete_returns_success_for_authenticated_user(self):
        """Test that authenticated user can use CFP API endpoint."""
        self.client.force_login(self.user)

        result = self.client.delete(CFP_URL + '{}/'.format(self.cfp.id))
        self.assertEqual(status.HTTP_204_NO_CONTENT, result.status_code, 'Status code should be 204 for delete.')
