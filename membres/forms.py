from django import forms
from .models import membres

class MembreForm(forms.ModelForm):
    class Meta:
        model = membres
        fields = ['nom', 'email', 'mot_de_passe', 'adresse', 'telephone']
