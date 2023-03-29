from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):

    content = "<html><body><h1> Welcome to little lemon crusade </h1></body></html>"
    return HttpResponse(content)

def say_hello(request):
    greeting = "Welcome to FelicityTech complany"
    return HttpResponse(greeting)

def homepage(request):
    return HttpResponse("welcome to group of complany")

