from django.shortcuts import render
from rdv.models import Rdv
# Create your views here.
def add_rdv(request):
    return render(request,'rdv/add_rdv.html')

def liste_rdv(request):
    rdv = Rdv.objects.all()
    context = {'rdv':rdv }
    #return render(request, 'acceuil/home.html', context)
    return render(request,'rdv/liste_rdv.html', context)
