from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def Home(request):
    return HttpResponse("Welcome to Little Lemon!")


def DateT(request):
    today = datetime.today()
    return HttpResponse(today)
