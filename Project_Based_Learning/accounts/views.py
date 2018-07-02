#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate, login
from student.models import Student
from teacher.models import Teacher
import json

class UserCreate(APIView): #Creates a user object based on the data sent from Client side and returns the token corresponding to the user
	"""
	Creates the user.
	"""
	permission_classes = (AllowAny,)
	def post(self, request, format='json'):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			#print("Valid")
			user = serializer.save()
			if user:
				if request.data["isStudent"] == 1:
					new_student = Student(user=user, contact_no=request.data["contact_no"])
					new_student.save()
				elif request.data["isStudent"] == 0:
					new_teacher = Teacher(user=user, contact_no=request.data["contact_no"])
					new_teacher.save()
				else:
					return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

				token = Token.objects.create(user=user)
				json = serializer.data
				json['token'] = token.key
				return Response(json, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView): #Logins the user based on username,password and isStudent field sent from Client Side and returns the corresponding token
	""" 
	Logs in the user. 
	"""
	permission_classes = (AllowAny,)
	def post(self,request,format='json'):
		username = request.data['username']
		password = request.data['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				print(request.data["isStudent"])
				if request.data["isStudent"] == 1:
					student = Student.objects.filter(user=user)

					#print(student)
					if len(student):
						login(request, user)
						token, created = Token.objects.get_or_create(user=user)
						js = json.dumps({"status" : "true", "token" : token.key})
						return Response(js, status=status.HTTP_200_OK)
					else:
						js = json.dumps({"status" : "false", "msg" : "Not a valid Student"})
						return Response(js, status=status.HTTP_400_BAD_REQUEST)
				else:
					teacher = Teacher.objects.filter(user=user)
					if len(teacher):
						login(request, user)
						token, created = Token.objects.get_or_create(user=user)
						js = json.dumps({"status" : "true", "token" : token.key})
						return Response(js, status=status.HTTP_200_OK)
					else:
						js = json.dumps({"status" : "false", "msg" : "Not a valid Teacher"})
						return Response(js, status=status.HTTP_400_BAD_REQUEST)

				
			else:
				js = json.dumps({"status" : "false", "reason" : "You need to activate your account. Please check your email"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)
		else:
				js = json.dumps({"status" : "false", "reason" : "Invalid username/password"})
				return Response(js, status=status.HTTP_400_BAD_REQUEST)


class UserInfo(APIView):
	""" 
	Logs in the user. 
	"""
	permission_classes = (AllowAny,)
	def get(self,request):
		currentUser = request.user
		print(currentUser)
		if currentUser.is_authenticated:
			#logged in user
			#print(currentUser)
			js = json.dumps({"status" : "true"})
			return Response(js, status=status.HTTP_200_OK)
		else:
			#anonymous user
			print("Not Signed In")
			js = json.dumps({"status" : "false", "reason" : "You need to sign in"})
			return Response(js, status=status.HTTP_401_UNAUTHORIZED)
			