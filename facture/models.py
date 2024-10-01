from django.db import models

# Create your models here.
"""
bills:
- nom du client
- date de la facture
- date pour la relance
    -email auto
    - msg alerte
-facture (img)
"""
class facture(models.Model):
    client_name = models.CharField(max_length=150, name='nom_du_client')
    facture_date = models.DateField(
        "Date de la facture (Jour/Mois/Année)", auto_now_add=False, auto_now=False, blank=True)
    facture_relance = models.DateField(
        "Date d'échéance (Jour/Mois/Année)", auto_now_add=False, auto_now=False, blank=True)
    facture_img = models.ImageField(upload_to='users/factures/', name='photo_de_la_facture')
