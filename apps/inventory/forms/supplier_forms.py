from django import forms
from apps.inventory.models import Supplier

        
class CreateSupplierForm(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = "__all__"

class UpdateSupplierForm(forms.ModelForm):
    
    class Meta:
        model = Supplier
        fields = "__all__"
