from django.db import models
from django.http import request
from django.shortcuts import render, redirect
from patient.models import Patient
from patient.forms import PatientForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='access')
def add_patient(request):
    return render(request, 'patient/add_patient.html')

def liste_patient(request):
        patients = Patient.objects.all()
        context = {'patients':patients }
        return render(request, 'patient/liste_patient.html', context)
     
def insert(request):
    if request.method == "POST":
        patient = Patient()
        patient.nom = request.POST.get("nom")
        patient.prenom = request.POST.get("prenom")
        patient.telephone = request.POST.get("telephone")
        patient.age = request.POST.get("age")
        patient.sexe = request.POST.get("sexe")
        patient.adresse = request.POST.get("adresse")
        print(request.POST)
        patient.save()
        return redirect ('/patient/liste')
    return render(request, 'patient/add_patient.html')
        
        
def modifier_patient(request, pk):
        patients = Patient.objects.get(id=pk)
        context={'patients':patients}
        patients.save()
        return render(request, 'patient/add_patient.html',context)   
        
 
             
def supprimer_patient(request, pk):
        patient = Patient()  
        patient = Patient.objects.get(id=pk)  
        #if request.method == "POST":
        patient.delete()       
        return redirect ('/patient/liste')  
    #return render(request, 'patient/liste_patient.html')