from django.shortcuts import redirect, render
from rdv.models import Rdv

# Create your views here.
def add_rdv(request):
    return render(request,'rdv/add_rdv.html')

def insert(request):
    if request.method == "POST":
        rdv = Rdv()
        rdv.nom = request.POST.get("nom")
        rdv.prenom = request.POST.get("prenom")
        rdv.dateRddv = request.POST.get("date_rdv")
        rdv.soins = request.POST.get("soins")
        rdv.save()
        return redirect ('/view')
    return render(request, 'patient/liste_patient.html')
        

def liste_rdv(request):
    rdv = Rdv.objects.all()
    context = {'rdv':rdv }
    return render(request,'rdv/liste_rdv.html', context)
  