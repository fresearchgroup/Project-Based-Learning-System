from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
	#pk is set by Django
	user = models.ForeignKey(User, related_name='teachers', on_delete=models.DO_NOTHING)
	contact_no = models.CharField(max_length=10)

	def __str__(self):
		return self.user.username + ':' + self.contact_not