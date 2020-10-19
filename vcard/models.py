from django.db import models

# Create your models here.
class vcard(models.Model):
    prenom = models.CharField(max_length=255, primary_key=True)
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    details = models.TextField()
