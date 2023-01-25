from django.urls import path
from . import views

urlpatterns = [
    path('getuser/', views.current_datetime),

]