from django.shortcuts import render
from .forms import CreateStudentForm
from .models import Student
from django.http import HttpResponse
# Create your views here.

def create_student(request):
