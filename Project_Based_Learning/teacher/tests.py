from django.test import TestCase
from django.contrib.auth.models import User
from .models import Teacher

# Create your tests here.
class TeacherTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="XYZ", last_name="PQR",email="xyz@gmail.com",username="xyzwu1928",password="xyzwu1928")
		user = User.objects.get(username="xyzwu1928",password="xyzwu1928")
		Teacher.objects.create(user=user, contact_no="0234567891")
		
	def test_teacher(self):
		
		user = User.objects.get(username="xyzwu1928",password="xyzwu1928")
		teacher = Teacher.objects.get(user=user)
		self.assertEqual(user is not None, True)
		self.assertEqual(teacher is not None, True)