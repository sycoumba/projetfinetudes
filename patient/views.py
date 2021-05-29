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
        patient = Patient.objects.all()
        context = {'patient':patient }
        return render(request, 'patient/liste_patient.html', context)
     
def insert(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/patient/liste')
    context={'form':form}
    return render(request, 'patient/add_patient.html', context)
 
        
        
def modifier_patient(request, pk):
    patient= Patient.objects.get(id=pk)
    form = PatientForm(instance=Patient)
    if request.method == "POST":
        form = PatientForm(request.POST,instance=Patient)   
        if form.is_valid():  
            form.save()
        return redirect('/patient/liste')
    context={'form':form}
    return render(request, 'patient/modifier_patient.html',context)   
        
 
             
def supprimer_patient(request, pk):
        patient = Patient()  
        patient = Patient.objects.get(id=pk)  
        #if request.method == "POST":
        patient.delete()       
        return redirect ('/patient/liste')  
    #return render(request, 'patient/liste_patient.html')