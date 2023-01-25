from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
    return HttpResponse("Name:{} userID:{}".format(name, id))