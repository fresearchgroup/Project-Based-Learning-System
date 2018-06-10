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

# Create your views here.

#List all teachers or create a new teacher
#teachers/
class ProjectList(APIView):

	def get(self, request):
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, many=True)
		return Response(serializer.data)

	def post(self):
		pass

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