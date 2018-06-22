from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = '__all__'
		extra_fields = ['projects', 'modules']
		depth = 1

	def get_field_names(self, declared_fields, info):
		expanded_fields = super(StudentSerializer, self).get_field_names(declared_fields, info)

		if getattr(self.Meta, 'extra_fields', None):
			return expanded_fields + self.Meta.extra_fields
		else:
			return expanded_fields