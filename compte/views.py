import compte
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreerUtilisateur
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def inscriptionPage(request):
    form= CreerUtilisateur()
    if request.method== 'POST': 
     form= CreerUtilisateur(request.POST)
     if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         messages.success(request,'Compte Créer avec Succes pour '+user)
         return redirect('access')
    context={'form':form}
    return render(request,'compte/inscription.html', context)

def home(request):
    return render(request, 'acceuil/home.html')

def accesPage(request):
    context={}
    if request.method== 'POST': 
         username =request.POST.get('username')
         password =request.POST.get('password')
         user = authenticate(request, username=username ,password=password)
         if user is not None:
             login(request,user)
             return redirect('accueil')
         else:
             messages.info(request,"utilisateur ou mot de passe incorrect")
    return render(request,'compte/access.html', context)

def logoutUser(request):
    logout(request)
    return redirect('access')
    
        