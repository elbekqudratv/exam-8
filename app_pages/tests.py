from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Contact, FAQ

class ContactViewTests(APITestCase):
    def setUp(self):
        self.url = reverse('contact-create')
        self.valid_payload = {
            'contact_name': 'elbekjon qudratov',
            'contact_sender': 'elbekjon@example.com',
            'contact_message': 'test case yoqdimi!'
        }
        self.invalid_payload = {
            'contact_name': '',
            'contact_sender': 'invalid-email',
            'contact_message': ''
        }

    def test_create_contact_valid_payload(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().contact_name, 'elbekjon qudratov')

    def test_create_contact_invalid_payload(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Contact.objects.count(), 0)


class FAQTests(APITestCase):
    def setUp(self):
        self.url = reverse('faq-list')
        self.valid_data = {
            'faq_question_uz': 'Test Question',
            'faq_answer_uz': 'Test Answer'
        }

    def test_create_faq(self):
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FAQ.objects.count(), 1)
