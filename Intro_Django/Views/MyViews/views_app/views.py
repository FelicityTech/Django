from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def home(request):

    content = "<html><body><h1> Welcome to little lemon crusade </h1></body></html>"
    return HttpResponse(content)


def say_hello(request):
    greeting = "Welcome to FelicityTech complany"
    return HttpResponse(greeting)


def homepage(request):
    return HttpResponse("welcome to group of complany")


def display_date(request):
    date_joined = datetime.today()
    return HttpResponse(date_joined)
