"""PBL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include,path
from .import views
from accounts import views as accounts_views
from rest_framework.urlpatterns import format_suffix_patterns
from teacher import views as teacher_views
from project_modules import views as project_modules_views
from student import views as student_views

urlpatterns = [
    url(r'^api-auth/userinfo/$', accounts_views.UserInfo.as_view(), name='account-info'),
    url(r'^api-auth/signin/$', accounts_views.UserLogin.as_view(), name='account-login'),
    url(r'^api-auth/signup/$', accounts_views.UserCreate.as_view(), name='account-create'),
    path('students/<int:id>/', student_views.StudentInfo.as_view()),
    url(r'^students/', student_views.StudentList.as_view()),
    path('modules/<int:id>/', project_modules_views.ModuleInfo.as_view()),
    url(r'^modules/', project_modules_views.ModuleList.as_view()),
    path('projects/<int:id>/', project_modules_views.ProjectInfo.as_view()),
    url(r'^projects/', project_modules_views.ProjectList.as_view()),
    path('teachers/<int:id>/', teacher_views.TeacherInfo.as_view()),
    url(r'^teachers/', teacher_views.TeacherList.as_view()),
    url('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)