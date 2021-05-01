from django.db.models import fields
from django import forms  
from django.forms import ModelForm
from .models import Rdv


class RdvForm(forms.ModelForm):
    class Meta:
        model = Rdv
        fields = '__all__'