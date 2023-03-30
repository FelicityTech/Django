from django.urls import path
from . import views

urlpatterns = [
    path('getuser/<name>/<id>', views.pathviews, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"),
]