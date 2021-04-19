from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.add_rdv, name='addrdv'),
   path('', views.liste_rdv, name='listerdv'),
]
