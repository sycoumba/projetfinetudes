from django.urls import path
from . import views

urlpatterns = [
  
    path('addrdv', views.add_rdv, name='addrdv'),
    path('listerdv', views.liste_rdv, name='listerdv'),
    path('modifier_rdv/<str:pk>', views.modifier_rdv, name='modifier_rdv'), 
    path('supprimer_rdv/<str:pk>', views.supprimer_rdv, name='supprimer_rdv'),   
  
]
