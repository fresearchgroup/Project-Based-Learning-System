from django.db import models
from teacher.models import Teacher
from student.models import Student
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Project(models.Model):
	project_name = models.CharField(max_length=100, unique=True)
	number_of_modules = models.IntegerField()
	#number_of_users = models.IntegerField()
	description = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	teacher = models.ForeignKey(Teacher, related_name='projects', on_delete=models.DO_NOTHING, null=True)
	students = models.ManyToManyField(Student,related_name='projects')

	def __str__(self):
		return self.project_name + ':' + str(self.number_of_modules) + ' ' + ' ' + self.description + ' ' 
		+ str(self.created_at) + ' ' + str(self.last_updated)

class Module(models.Model):
	module_name = models.CharField(max_length=100, unique=True)
	dependencies = models.ManyToManyField('self', symmetrical=False)
	code = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	project = models.ForeignKey(Project, related_name='modules', on_delete=models.DO_NOTHING, null=True)
	students = models.ManyToManyField(Student, related_name='modules')
	color = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(2), MinValueValidator(0)]
     ) # 0: untouched, 1: in-progress, 2: completed

	def __str__(self):
		return self.module_name
