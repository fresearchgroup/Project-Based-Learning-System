from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .models import Student
from rest_framework import status
from .serializers import StudentSerializer

# Create your views here.


class StudentList(APIView): #returns the list of students signed in

	def get(self, request):
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class StudentInfo(generics.ListAPIView):
	serializer_class = StudentSerializer
	lookup_url_kwarg = "id"

	def get_queryset(self):
		id = self.kwargs.get(self.lookup_url_kwarg)
		return Student.objects.filter(id=id)