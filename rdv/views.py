from django.shortcuts import redirect, render
from rdv.models import Rdv
from rdv.forms import RdvForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='access')
def add_rdv(request):
    return render(request,'rdv/add_rdv.html')

def insert(request):
    form = RdvForm()
    
    
'''  if request.method == "POST":
        rdv = Rdv()
        rdv.patient = request.POST.get("nom")
        rdv.date_rdv= request.POST.get("date_rdv")
        rdv.soins = request.POST.get("soins")
        rdv.save()
        return redirect ('/rdv/liste')
    return render(request, 'patient/liste_patient.html')
         '''

def liste_rdv(request):
    rdv = Rdv.objects.all()
    context = {'rdv':rdv }
    return render(request,'rdv/liste_rdv.html', context)
  