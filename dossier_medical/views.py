from django.shortcuts import render

# Create your views here.


def add_dossier(request):
    return render(request, 'dossier_medical/add_dossier.html')


def liste_dossier(request):
    return render(request, 'dossier_medical/liste_dossier.html')