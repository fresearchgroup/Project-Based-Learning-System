from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Project
from .models import Module
from rest_framework import status
from .serializers import ProjectSerializer
from .serializers import ModuleSerializer
import json
from .models import Project
from .models import Module
from teacher.models import Teacher
from student.models import Student

# Create your views here.

#List all teachers or create a new teacher
#teachers
class ProjectList(APIView):

	def get(self, request):
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, many=True)
		return Response(serializer.data)

	def post(self, request, format='json'):
		user = request.user
		if user is not None:
			if user.is_active:
				teacher_user = Teacher.objects.filter(user=user)
				if len(teacher_user):
					data = request.data
					project = Project(project_name=data['project_name'], description=data['description'], number_of_modules=data['number_of_modules']);
					project.save()
					modules = data['modules']
					for i in modules:
						module = Module(module_name=i['module_name'], description=i['description'])
						module.save()
						project.modules.add(module)

					project.save()
					teacher_user[0].projects.add(project)
					teacher_user[0].save()
					js = json.dumps({"status" : "true", "msg" : "Project Successfully Added"})
					return Response(js, status=status.HTTP_201_CREATED)
				else:
					js = json.dumps({"status" : "false", "msg" : "Not a valid Student"})
					return Response(js, status=status.HTTP_400_BAD_REQUEST)
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
				js = json.dumps({"status" : "false", "reason" : "Please login and try again"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		

		print(user.username)
		print(request.data)
		

class ProjectInfo(generics.ListAPIView):
	serializer_class = ProjectSerializer
	lookup_url_kwarg = "id"

	def get_queryset(self):
		id = self.kwargs.get(self.lookup_url_kwarg)
		return Project.objects.filter(id=id)

class ModuleList(APIView):

	def get(self, request):
		modules = Module.objects.all()
		serializer = ModuleSerializer(modules, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class ModuleInfo(generics.ListAPIView):
	serializer_class = ModuleSerializer
	lookup_url_kwarg = "id"

	def get_queryset(self):
		id = self.kwargs.get(self.lookup_url_kwarg)
		return Module.objects.filter(id=id)