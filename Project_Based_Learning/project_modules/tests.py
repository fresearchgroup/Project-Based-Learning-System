from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project
from .models import Module
from teacher.models import Teacher
from student.models import Student

# Create your tests here.
class ProjectTestCase(TestCase):
	def setUp(self):
		User.objects.create(first_name="XYZ", last_name="PQR",email="xyz@gmail.com",username="xyzwu1928",password="xyzwu1928")
		user = User.objects.get(username="xyzwu1928",password="xyzwu1928")
		Teacher.objects.create(user=user, contact_no="0234567891")
		teacher = Teacher.objects.get(user=user)
		Project.objects.create(teacher=teacher,project_name="C++",description="C++ Learning",number_of_modules=2)
		
	def test_project(self):
		
		user = User.objects.get(username="xyzwu1928",password="xyzwu1928")
		teacher = Teacher.objects.get(user=user)
		project = Project.objects.get(project_name="C++")
		self.assertEqual(project is not None, True)
		self.assertEqual(project.teacher, teacher)
		self.assertEqual(project.description, "C++ Learning")


class ModulesTestCase(TestCase):
	def setUp(self):
		#create teacher
		User.objects.create(first_name="XYZ", last_name="PQR",email="xyz@gmail.com",username="xyzwu1928",password="xyzwu1928")
		user = User.objects.get(username="xyzwu1928",password="xyzwu1928")
		Teacher.objects.create(user=user, contact_no="0234567891")
		teacher = Teacher.objects.get(user=user)
		#create student1
		User.objects.create(first_name="Student1", last_name="PQR",email="student1@gmail.com",username="student11928",password="student11928")
		user = User.objects.get(username="student11928",password="student11928")
		Student.objects.create(user=user,contact_no="12345")
		student1 = Student.objects.get(user=user)
		#create student2
		User.objects.create(first_name="Student2", last_name="PQR",email="student2@gmail.com",username="student21928",password="student21928")
		user = User.objects.get(username="student21928",password="student21928")
		Student.objects.create(user=user,contact_no="123456")
		student2 = Student.objects.get(user=user)
		#create Project and assign it to teacher
		Project.objects.create(teacher=teacher,project_name="C++",description="C++ Learning",number_of_modules=2)
		project = Project.objects.get(project_name="C++")
		#create module1
		Module.objects.create(module_name="Functions",description="Learn Functions")
		module1 = Module.objects.get(module_name="Functions")
		#assign module1 to both students
		module1.students.add(student1)
		module1.students.add(student2)
		#create module2
		Module.objects.create(module_name="Addition",description="Learn Addition")
		module2 = Module.objects.get(module_name="Addition")
		#assign module1 to student2
		module2.students.add(student2)
		#module1 depends on module2
		module1.dependencies.add(module2)
		#add modules to the project created
		project.modules.add(module1)
		project.modules.add(module2)


		
	def test_module(self):
		
		user = User.objects.get(username="xyzwu1928",password="xyzwu1928")
		teacher = Teacher.objects.get(user=user)
		project = Project.objects.get(project_name="C++")
		module1 = Module.objects.get(module_name="Functions")
		module2 = Module.objects.get(module_name="Addition")
		user = User.objects.get(username="student21928",password="student21928")
		student2 = Student.objects.get(user=user)
		self.assertEqual(project.teacher, teacher)
		self.assertEqual(len(project.modules.all()), project.number_of_modules)
		self.assertEqual(len(module1.students.all()), 2)
		self.assertEqual(len(module2.students.all()), 1)
		self.assertEqual(len(module1.dependencies.all()), 1)
		self.assertEqual((module1.dependencies.all())[0], module2)
		self.assertEqual(len(student2.modules.all()), 2)
		
		
		