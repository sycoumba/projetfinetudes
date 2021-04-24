from django.db import models
from django.shortcuts import render, redirect
from patient.models import Patient
from patient.forms import PatientForm


# Create your views here.


def add_patient(request):
    return render(request, 'patient/add_patient.html')

def insert(request):
    if request.method == "POST":
        patient = Patient()
        patient.nom = request.POST.get("nom")
        patient.prenom = request.POST.get("prenom")
        patient.telephone = request.POST.get("telephone")
        patient.age = request.POST.get("age")
        patient.sexe = request.POST.get("sexe")
        patient.adresse = request.POST.get("adresse")
        patient.save()
        return redirect ('/patient/liste')
    return render(request, 'patient/add_patient.html')
        
        
def modifier_patient(request, pk):
    
    patient = Patient.objects.get(id=pk)
    
    if request.method == "POST":
        patient = Patient()
        patient.nom = request.POST.get("nom")
        patient.prenom = request.POST.get("prenom")
        patient.telephone = request.POST.get("telephone")
        patient.age = request.POST.get("age")
        patient.sexe = request.POST.get("sexe")
        patient.adresse = request.POST.get("adresse")
        patient.save()
        return redirect ('/patient/add')
    return render(request, 'patient/add_patient.html')
             
        
        
        
''' form = PatientForm(request.POST)
            if form.is_valid():
                try:
                  form.save()
                  return redirect('patient/liste_patient.html')
                except:
                    pass
        
    else:
        form = PatientForm()
    return render(request,'patient/add_patient.html', {'form': form})
        
         '''

def liste_patient(request):
   patients = Patient.objects.all()
   context = {'patients':patients }
   return render(request, 'patient/liste_patient.html', context) 

''' def insert(request):
    if request.method == "POST":
            form = PatientForm(request.POST)
            if form.is_valid:
                form.save(commit=False)
                ip_address = get_patient_ip(request)
                form.ip = ip_address
                form.save()
            else:
                error= "empty fields"
                return render(request, 'registration/content.html',{'error': error,'form':form})
    else:
            form = RestaurantForm()
            return render(request, 'registration/content.html',{'form': form}) '''