from django import forms
from .models import facture


class FactureForm(forms.ModelForm):

    class Meta:
        model = facture
        fields = (
            'nom_du_client', 'facture_date', 'facture_relance', 'photo_de_la_facture',
        )
