from rest_framework.test import APITestCase
from rest_framework import status
from pyconbalkan.contact.models import Contact


class ContactTests(APITestCase):
    def test_contact_valid(self):
        number_existing_contacts = Contact.objects.count()
        data = {'name': 'client_name', 'company': '', 'email': 'client@client.com', 'message': 'Hi.....'}
        response = self.client.post('/api/contact/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), number_existing_contacts + 1)

    def test_contact_invalid(self):
        data = {'name': 'client_name', 'company': '', 'email': 'clientlient.com', 'message': 'Hi.....'}
        response = self.client.post('/api/contact/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
