from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):

	class Meta:
		model = Teacher
		fields = '__all__'
		extra_fields = ['projects']
		depth = 1

	def get_field_names(self, declared_fields, info):
		expanded_fields = super(TeacherSerializer, self).get_field_names(declared_fields, info)

		if getattr(self.Meta, 'extra_fields', None):
			return expanded_fields + self.Meta.extra_fields
		else:
			return expanded_fields