from django import forms
from apps.inventory.models import Facture

        
class CreateFactureForm(forms.ModelForm):
    
    class Meta:
        model = Facture
        fields = "__all__"

class UpdateFactureForm(forms.ModelForm):
    
    class Meta:
        model = Facture
        fields = "__all__"
