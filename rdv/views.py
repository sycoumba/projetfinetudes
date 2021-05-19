from django.shortcuts import redirect, render
from rdv.models import Rdv
from patient.models import Patient
from rdv.forms import RdvForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='access')

def add_rdv(request):
    patient=Patient.objects.all()
    return render(request,'rdv/add_rdv.html',{'patient':patient})

def liste_rdv(request):
    rdv = Rdv.objects.all()
    context = {'rdv':rdv }
    return render(request,'rdv/liste_rdv.html', context)

def insert_rdv(request):
    if request.method == "POST":
        rdv = Rdv()
        rdv.patient_id= request.POST.get("patient_id")
        rdv.date_rdv= request.POST.get("date_rdv")
        rdv.soins = request.POST.get("soins")
        print(request.POST)
        rdv.save()
        return redirect ('/rdv/listerdv')
    return render(request, 'rdv/liste_rdv.html')
         
def modifier_rdv(request, pk):
    rdv = Rdv.objects.get(id=pk)
    context={'rdv':rdv}
    return render(request, 'rdv/add_rdv.html',context)   
def supprimer_rdv(request, pk):
        rdv = Rdv.objects.get(id=pk)  
        rdv.delete()       
        return redirect ('/rdv/listerdv')  
    
def total_rdv(request):
    # rdv= Rdv()
    rdv = Rdv.objects.all()
    patient=Patient.objects.all()
    total_rdv= rdv.count()
    context={'rdv':rdv, 'patient':patient,'total_rdv':total_rdv}
    return render(request, 'accueil/home.html',context)  
       
             
             
  