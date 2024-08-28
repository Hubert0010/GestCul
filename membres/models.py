from django.db import models


# Create your models here.

class membres(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Assurez-vous que l'email est unique
    mot_de_passe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.nom 
