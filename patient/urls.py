from django.urls import path
from . import views

urlpatterns = [
  
    path('add', views.add_patient, name='add'),
    path('liste', views.liste_patient, name='liste'), 
    path('insert', views.insert, name='insert'), 
    path('modifier_patient/<str:pk>', views.modifier_patient, name='modifier_patient'), 
  
  
]
