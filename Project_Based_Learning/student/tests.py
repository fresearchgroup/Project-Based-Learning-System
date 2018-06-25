from django.test import TestCase
from django.contrib.auth.models import User
from .models import Student

# Create your tests here.
class StudentTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="PQR", last_name="XYZ",email="pqr@gmail.com",username="pqrst1928",password="pqrst1928")
		user = User.objects.get(username="pqrst1928",password="pqrst1928")
		Student.objects.create(user=user, contact_no="1234567890")
		
	def test_student(self):
		"""Animals that can speak are correctly identified"""
		user = User.objects.get(username="pqrst1928",password="pqrst1928")
		student = Student.objects.get(user=user)
		self.assertEqual(user is not None, True)
		self.assertEqual(student is not None, True)