from django.urls import path
from . import views

urlpatterns = [
  
    path('addrdv', views.add_rdv, name='addrdv'),
    path('listerdv', views.liste_rdv, name='listerdv'),

]
