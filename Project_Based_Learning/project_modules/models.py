from django.db import models
from teacher.models import Teacher
from student.models import Student

# Create your models here.
class Project(models.Model):
	project_name = models.CharField(max_length=100, unique=True)
	number_of_modules = models.IntegerField()
	number_of_users = models.IntegerField()
	description = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	teacher_id = models.ForeignKey(Teacher, related_name='projects', on_delete=models.DO_NOTHING, null=True)

	def __str__(self):
		return self.project_name + ':' + str(self.number_of_modules) + ' ' + str(self.number_of_users) + ' ' + self.description + ' ' 
		+ str(self.created_at) + ' ' + str(self.last_updated) + ' ' + self.teacher_id

class Module(models.Model):
	module_name = models.CharField(max_length=100, unique=True)
	dependancies = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	teacher_id = models.ForeignKey(Teacher, related_name='modules', on_delete=models.DO_NOTHING, null=True)
	student_id = models.ForeignKey(Student, related_name='modules', on_delete=models.DO_NOTHING, null=True)

	def __str__(self):
		return self.module_name + ' :' + self.description + ' ' + self.teacher_id.user.username + ' ' + self.student_id.user.username