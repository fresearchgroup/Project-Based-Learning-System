from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Project
from .models import Module
from rest_framework import status
from .serializers import ProjectSerializer
from django.contrib.auth.models import User
from .serializers import ModuleSerializer
import json
from .models import Project
from .models import Module
from teacher.models import Teacher
from student.models import Student
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


# Create your views here.

class StudentProjectList(APIView):

	def get(self, request):
		user = request.user
		if user is not None:
			if user.is_active:
				student_user = Student.objects.filter(user=user)
				if len(student_user):
					modules = student_user[0].modules.all()
					serializer = ModuleSerializer(modules, many=True)
					return Response(serializer.data)
				else:
					js = json.dumps({"status" : "false", "msg" : "Not a valid Student"})
					return Response(js, status=status.HTTP_400_BAD_REQUEST)
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
			js = json.dumps({"status" : "false", "reason" : "Please login and try again"})
			return Response(js, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format='json'):
		pass
		

#List all teachers or create a new teacher
#teachers
class TeacherProjectList(APIView):

	def get(self, request):
		user = request.user
		if user is not None:
			if user.is_active:
				teacher_user = Teacher.objects.filter(user=user)
				if len(teacher_user):
					projects = teacher_user[0].projects.all()
					serializer = ProjectSerializer(projects, many=True)
					return Response(serializer.data)
				else:
					js = json.dumps({"status" : "false", "msg" : "Not a valid Teacher"})
					return Response(js, status=status.HTTP_400_BAD_REQUEST)
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
			js = json.dumps({"status" : "false", "reason" : "Please login and try again"})
			return Response(js, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format='json'):
		user = request.user
		if user is not None:
			if user.is_active:
				teacher_user = Teacher.objects.filter(user=user)
				if len(teacher_user):
					# json_data = json.loads(str(request.body, encoding='utf-8'))
					# serializer = ProjectSerializer(data=json_data)
					# if serializer.is_valid():
					# 	project = serializer.save()
					data = request.data
					
					modules = data['modules']
					for i in modules:
						for j in i['students']:
							print(j)
							user = User.objects.filter(username=j)
							if not len(user):
								print("HI")
								js = json.dumps({"status" : "false", "msg" : "Enter correct username"})
								return Response(js, status=status.HTTP_400_BAD_REQUEST)
							else:
								student = Student.objects.get(user=user[0])
								if student:
									continue
								else:
									js = json.dumps({"status" : "false", "msg" : "Enter correct username"})
									return Response(js, status=status.HTTP_400_BAD_REQUEST)
					project = Project.objects.filter(project_name=data['project_name'])
					if len(project):
						print("HI")
						js = json.dumps({"status" : "false", "msg" : "Enter new project name"})
						return Response(js, status=status.HTTP_400_BAD_REQUEST)
					project = Project(project_name=data['project_name'], description=data['description'], number_of_modules=data['number_of_modules']);
					project.save()
					for i in modules:
						module = Module(module_name=i['module_name'], description=i['description'])
						module.save()
						project.modules.add(module)

					for i in modules:
						module = Module.objects.filter(module_name=i['module_name'], description=i['description'])
						module1 = module[0]
						module1.dependencies.clear()
						for j in i['dependencies']:
							inner_module = Module.objects.filter(module_name=j['module_name'], description=j['description'])
							module1.dependencies.add(inner_module[0])

						for j in i['students']:
							user = User.objects.get(username=j)
							student = Student.objects.get(user=user)
							module1.students.add(student)

						print(module1.dependencies.all())
						print(module1.students.all())
						module1.save()

					project.save()
					teacher_user[0].projects.add(project)
					teacher_user[0].save()
					js = json.dumps({"status" : "true", "msg" : "Project Successfully Added"})
					return Response(js, status=status.HTTP_201_CREATED) 
					
				else:
					js = json.dumps({"status" : "false", "msg" : "Not a valid Teacher"})
					return Response(js, status=status.HTTP_400_BAD_REQUEST)
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
			js = json.dumps({"status" : "false", "reason" : "Please login and try again"})
			return Response(js, status=status.HTTP_400_BAD_REQUEST)
		

		print(user.username)
		print(request.data)
		

class ProjectInfo(APIView):

	def get(self, request, project_name):
		user = request.user
		if user is not None:
			if user.is_active:
				teacher_user = Teacher.objects.filter(user=user)
				if len(teacher_user):
					# json_data = json.loads(str(request.body, encoding='utf-8'))
					# serializer = ProjectSerializer(data=json_data)
					# if serializer.is_valid():
					# 	project = serializer.save()
					path = request.get_full_path()
					
					path = path.split('/')
					print(path)
					project = Project.objects.get(project_name=path[2],teacher=teacher_user[0])
					if(project):
						proj = project
						#send project info
						serializer = ProjectSerializer(proj)
						return Response(serializer.data, status=status.HTTP_201_CREATED) #change to 200 success
					else:
						js = json.dumps({"status" : "false", "msg" : "Not a valid Project"})
						return Response(js, status=status.HTTP_400_BAD_REQUEST)
					
				else:
					js = json.dumps({"status" : "false", "msg" : "Not a valid Teacher"})
					return Response(js, status=status.HTTP_400_BAD_REQUEST)
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
				js = json.dumps({"status" : "false", "reason" : "Please login and try again"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format='json'):
		pass

def make_graph(project):
	nodes = []
	edges = []
	for module in project.modules.all():
		_node = {'id': module.id, 'label': module.module_name, 'title': module.module_name}
		_node['color'] = '#00e676'
		nodes += [_node]

	for module in project.modules.all():
		target_id = module.id
		for j in module.dependencies.all():
			source_id = j.id
			edges += [{'from': source_id, 'to': target_id, 'label': '', 'arrows': 'to'}]

	return nodes,edges



class GetGraph(APIView):

	def get(self, request, project_name):
		user = request.user
		if user is not None:
			if user.is_active:
				
				path = request.get_full_path()
				path = path.split('/')
				print(path)
				project = Project.objects.get(project_name=path[2])
				if(project):
					proj = project
					#send project info
					nodes,edges = make_graph(project)
					# serializer = ProjectSerializer(proj)
					return JsonResponse({'project_name': project.project_name, 'nodes': json.dumps(nodes), 'edges': json.dumps(edges)})
				else:
					js = json.dumps({"status" : "false", "msg" : "Not a valid Project"})
					return Response(js, status=status.HTTP_400_BAD_REQUEST)
					
				
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
				js = json.dumps({"status" : "false", "reason" : "Please login and try again"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, format='json'):
		pass