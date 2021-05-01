from django.urls.conf import path
from django.urls.resolvers import URLPattern
from .import views 
from django .urls import path

urlpatterns=[
    
    path('',views.inscriptionPage, name='inscription'),
    path('index', views.home, name ='accueil'),
    path('access',views.accesPage, name='access'),
    path('quitter',views.logoutUser, name='quitter'),
    ]