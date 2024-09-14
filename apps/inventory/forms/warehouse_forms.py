from django import forms
from apps.inventory.models import Warehouse

        
class CreateWarehouseForm(forms.ModelForm):
    
    class Meta:
        model = Warehouse
        fields = "__all__"

class UpdateWarehouseForm(forms.ModelForm):
    
    class Meta:
        model = Warehouse
        fields = "__all__"
