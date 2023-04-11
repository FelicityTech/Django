import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    viewer = get_template('SviewApp/index.html')
    return HttpResponse(viewer)