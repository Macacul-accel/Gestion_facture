from django.db import models

# Create your models here.

class Factures(models.Model):
    client_name = models.CharField(max_length=150, name='nom_client')
    facture_date = models.DateField(
        "Date de la facture (Jour/Mois/Année)", auto_now_add=False, auto_now=False, blank=True)
    facture_relance = models.DateField(
        "Date d'échéance (Jour/Mois/Année)", auto_now_add=False, auto_now=False, blank=True)
    facture_img = models.ImageField(upload_to='users/factures/', null=False, blank=False, name='photo_facture')


    def delete(self, *args, **kwargs):
        self.photo_facture.delete()
        super().delete(*args, **kwargs)
