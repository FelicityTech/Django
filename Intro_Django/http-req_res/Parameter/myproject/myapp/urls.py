from django.urls import path
from views import views

urlpatterns = [path('getuser/<name>/<id>', views.pathview, name='pathview'),]