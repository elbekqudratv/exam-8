from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
import json

User = get_user_model()

class RegisterAPIViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_user(self):
        
        user_data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'test_password',
            'first_name': 'Test',
            'last_name': 'User',
            'birth_date': '2000-01-01',
            'organization': 'Test Organization',
            'scientific_degree': 'Ph.D.',
            'info': 'Test user information'
        }
        
        response = self.client.post(self.register_url, user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'test_user')

class PasswordChangeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.password_change_url = reverse('password_change')

        
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='test_password')

    def test_password_change(self):
        
        self.client.login(username='test_user', password='test_password')

        
        password_change_data = {
            'old_password': 'test_password',
            'new_password': 'new_test_password'
        }
        
        response = self.client.post(self.password_change_url, password_change_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.user.refresh_from_db()
        
        self.assertTrue(self.user.check_password('new_test_password'))


