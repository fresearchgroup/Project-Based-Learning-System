from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Teacher
from rest_framework import status
from .serializers import TeacherSerializer

# Create your views here.

#List all teachers or create a new teacher
#teachers/
class TeacherList(APIView):

	def get(self, request):
		teachers = Teacher.objects.all()
		serializer = TeacherSerializer(teachers, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class TeacherInfo(generics.ListAPIView):
	serializer_class = TeacherSerializer
	lookup_url_kwarg = "id"

	def get_queryset(self):
		id = self.kwargs.get(self.lookup_url_kwarg)
		return Teacher.objects.filter(id=id)