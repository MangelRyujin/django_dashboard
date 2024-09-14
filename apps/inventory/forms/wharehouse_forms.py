from django import forms
from apps.inventory.models import Wharehouse

        
class CreateWharehouseForm(forms.ModelForm):
    
    class Meta:
        model = Wharehouse
        fields = "__all__"

class UpdateWharehouseForm(forms.ModelForm):
    
    class Meta:
        model = Wharehouse
        fields = "__all__"
