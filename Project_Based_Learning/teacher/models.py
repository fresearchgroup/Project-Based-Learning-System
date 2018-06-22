from django.db import models
from django.contrib.auth.models import User
from student.models import Student

# Create your models here.
class Teacher(models.Model):
	#pk is set by Django
	user = models.ForeignKey(User, related_name='teachers', on_delete=models.DO_NOTHING)
	contact_no = models.CharField(max_length=10)
	students = models.ManyToManyField(Student,related_name='teacher')

	def __str__(self):
		return self.user.username + ':' + self.contact_no

		

'''
class Teacher_Student(models.Model):
	teacher = models.ForeignKey(Teacher,related_name='teachers',on_delete=models.DO_NOTHING)
	students = models.ManyToManyField(Student,related_name='teachers')
	'''