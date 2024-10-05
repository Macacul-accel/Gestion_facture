from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Factures(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    facture_name = models.CharField(max_length=150,blank=False, name='nom_facture')
    client_name = models.CharField(max_length=150, name='nom_client')
    facture_date = models.DateField(
        "Date de la facture (Jour/Mois/Année)", auto_now_add=False, auto_now=False, blank=True, null=False)
    facture_relance = models.DateField(
        "Date d'échéance (Jour/Mois/Année)", auto_now_add=False, auto_now=False, blank=True)
    facture_img = models.ImageField(upload_to=user_directory_path, null=False, blank=False, name='photo_facture')

    def __str__(self):
        return self.facture_name

    def delete(self, *args, **kwargs):
        self.photo_facture.delete()
        super().delete(*args, **kwargs)
