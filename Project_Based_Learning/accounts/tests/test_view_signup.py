from django.contrib.auth.models import User
#from django.contrib.auth.forms import SignUpForm
from django.urls import resolve
from django.urls import reverse
from django.test import TestCase
from ..views import  signup
from ..forms import SignUpForm



# Create your tests here.

class SignUpTests(TestCase):
	def setUp(self):
		url = reverse('signup')
		self.response = self.client.get(url)

	def test_signup_status_code(self):
		url = reverse('signup')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_signup_url_resolves_signup_view(self):
		view = resolve('/signup/')
		self.assertEquals(view.func, signup)

	def test_csrf(self):
		self.assertContains(self.response, 'csrfmiddlewaretoken')

	def test_contains_form(self):
		form = self.response.context.get('form')
		self.assertIsInstance(form, SignUpForm)

	def test_form_inputs(self):
		self.assertContains(self.response, '<input',8)
		self.assertContains(self.response, 'type="last_name"', 0)
		self.assertContains(self.response, 'type="first_name"', 0)
		self.assertContains(self.response,'type="contact_no"',0)
		self.assertContains(self.response, 'type="email"', 1)
		self.assertContains(self.response, 'type="password"', 2)
		#self.assertContains(self.response, 'type="password2"', 1)
		self.assertContains(self.response, 'type="username"', 0)
		


class SuccessfulSignUpTests(TestCase):
	def setUp(self):
		url = reverse('signup')
		data = {
			'first_name':'anshuman',
			'last_name':'chaursiya',
			'contact_no':'1234567890',
			'email' : 'ansh9010@gmail.com',
            'username': 'john',
			'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
		self.response = self.client.post(url, data)
		self.home_url = reverse('home')

	def test_redirection(self):
		self.assertRedirects(self.response, self.home_url)

	def test_user_creation(self):
		self.assertTrue(User.objects.exists())

	def test_user_authentication(self):
        
		response = self.client.get(self.home_url)
		user = response.context.get('user')
		self.assertTrue(user.is_authenticated)


class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  

    def test_signup_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())