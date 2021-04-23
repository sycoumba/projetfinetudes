from django.shortcuts import render
from rdv.models import Rdv
from patient.models import Patient
# Create your views here.
def connexion(request):
    return render(request, 'acceuil/login.html')

def home(request):
    rdv = Rdv.objects.all()
    patients = Patient.objects.all()
    context = {'rdv':rdv , 'patient':patients}
    return render(request, 'acceuil/home.html', context)
