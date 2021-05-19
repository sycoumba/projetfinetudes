from django.urls import path
from . import views

urlpatterns = [
  
    path('add_dossier', views.add_dossier, name='add_dossier'),
     path('liste_dossier', views.liste_dossier, name='liste_dossier'),
]