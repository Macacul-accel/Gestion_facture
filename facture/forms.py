from django import forms
from .models import Factures


class FactureForm(forms.ModelForm):

    class Meta:
        model = Factures
        fields = (
            'nom_facture' ,'nom_client', 'facture_date', 'facture_relance', 'photo_facture',
        )
