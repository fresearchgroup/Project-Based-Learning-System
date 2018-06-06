from django.test import TestCase
from ..forms import SignUpForm


class SignUpFormTest(TestCase):
	def test_form_has_fields(self):
		form = SignUpForm()
		expected = ['first_name','last_name','contact_no','email','username',  'password1', 'password2',]
		actual = list(form.fields)
		self.assertSequenceEqual(expected, actual)