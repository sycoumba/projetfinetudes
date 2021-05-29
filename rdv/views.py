from django.shortcuts import redirect, render
from rdv.models import Rdv
from patient.models import Patient
from rdv.forms import RdvForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='access')

def add_rdv(request):
    # patients should be plural, we're retrieving all the patients
    patients = Patient.objects.all()
    return render(request,'rdv/add_rdv.html',{'patients':patients})

def liste_rdv(request):
    rdv = Rdv.objects.all()
    context = {'rdv':rdv }
    return render(request,'rdv/liste_rdv.html', context)

# there should be a method for addition
# and another method for modification
def insert_rdv(request):
    if request.method == "POST":
        rdv_pk = request.POST.get("rdv_pk")
        if rdv_pk: # if there is an rdvid ---> modification
            rdv_pk = int(rdv_pk)
            rdv = Rdv.objects.get(pk=rdv_pk)
        else: # no id ---> it's an addition
            rdv = Rdv()
        rdv.patient = Patient.objects.get(
            pk=int(request.POST.get("patient_pk"))
        )
        rdv.date_rdv = request.POST.get("date_rdv")
        rdv.soins = request.POST.get("soins")
        rdv.save()
    # whatever the scenario, alway redirect to listrdv
    return redirect('/rdv/listerdv')


def modifier_rdv(request, pk):
    rdv = Rdv.objects.get(id=pk)
    # obviously, you also want to retrieve all the patients
    patients = Patient.objects.all()
    context = {'rdv': rdv, 'patients': patients}
    # it's a better idea to have a template for addition
    # and another template for modification
    return render(request, 'rdv/add_rdv.html', context)

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
