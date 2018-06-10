from rest_framework import serializers
from .models import Project
from .models import Module

class ProjectSerializer(serializers.ModelSerializer):

	class Meta:
		model = Project
		fields = '__all__'
		extra_fields = ['modules']
		depth = 1

	def get_field_names(self, declared_fields, info):
		expanded_fields = super(ProjectSerializer, self).get_field_names(declared_fields, info)

		if getattr(self.Meta, 'extra_fields', None):
			return expanded_fields + self.Meta.extra_fields
		else:
			return expanded_fields	

class ModuleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Module
		fields = '__all__'
		extra_fields = ['students', 'dependencies']
		depth = 1

	def get_field_names(self, declared_fields, info):
		expanded_fields = super(ModuleSerializer, self).get_field_names(declared_fields, info)

		if getattr(self.Meta, 'extra_fields', None):
			return expanded_fields + self.Meta.extra_fields
		else:
			return expanded_fields