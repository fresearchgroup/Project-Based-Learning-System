from django.db import models
from django.contrib.auth.models import User
#from teacher.models import Teacher

# Create your models here.
class Student(models.Model):
	#pk is set by Django
	user = models.ForeignKey(User, related_name='student', on_delete=models.DO_NOTHING)
	contact_no = models.CharField(max_length=10, unique=True)
	#teacher_id = models.ForeignKey(Teacher, related_name='student', on_delete=models.DO_NOTHING, null=True)

	def __str__(self):
		return self.user.username + ':' + self.contact_no