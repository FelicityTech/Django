from django.urls import path
from . import views

app_name = 'regexapp'

urlpatterns = [
    path('', views.index, name='index'),
]
