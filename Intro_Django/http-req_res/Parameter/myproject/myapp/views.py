from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def pathview(request, name, id):
    return HttpResponse("Name:{} UserID:{}".format(name, id))
