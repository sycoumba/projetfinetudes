from django.db import models


# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=150)
    age = models.TextField(null=True)
    sexe = models.TextField(null=True)
    adresse = models.TextField(null=False)
    
    class Meta:
     db_table = "patient"
   
    def __str__(self):
    
      return self.nom + " " + self.prenom

    