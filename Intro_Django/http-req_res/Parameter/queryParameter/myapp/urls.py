from django.urls import path
from views import views

urlpatterns = [
    path('getuser/', views.qryview, name='qryview'),

]