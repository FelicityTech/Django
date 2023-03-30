from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . import templates

def pathviews(request, name, id):

    return HttpResponse(f"Name:{name}   UserID:{id}")

# Query Parameter 

def qryview(request):

    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse(f"Name:{name} UserID: {id}")


# http://127.0.0.1:8000/getuser/?name=john&id=13

def showform(request):
    return render(request, 'templates/form.html')