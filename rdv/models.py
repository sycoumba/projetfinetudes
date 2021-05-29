from django.db import models
from patient.models import Patient

# Create your models here.
class Rdv(models.Model):
    date_rdv = models.DateTimeField(blank=True, null=True)
    soins = models.CharField(max_length=150)
    # a patient can have zero or many rdv
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
     db_table = "rdv"
