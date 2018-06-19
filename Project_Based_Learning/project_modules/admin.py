from django.contrib import admin

# Register your models here.
from .models import Project
from .models import Module

admin.site.register(Project)
admin.site.register(Module)