from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate

def home(request):
	return render(request,'index.html')

