from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm
from .views import SignupPageView

class SignupPageViewTest(TestCase):
    def setUp(self):
        self.url = reverse('accounts:signup')
        self.user_data = {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
    
    def test_signup_page_render(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)
    
    def test_signup_form_submission(self):
        response = self.client.post(self.url, data=self.user_data)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(get_user_model().objects.filter(username='testuser').exists())
    
    def test_signup_form_invalid_submission(self):
        self.user_data['password2'] = 'differentpassword'
        response = self.client.post(self.url, data=self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].has_error('password2'))

