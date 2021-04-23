from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.connexion),
    path('index', views.home, name ='accueil'),
  
]
