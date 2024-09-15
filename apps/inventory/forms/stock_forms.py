from django import forms
from apps.inventory.models import Stock

        
class CreateStockForm(forms.ModelForm):
    
    class Meta:
        model = Stock
        fields = "__all__"

class UpdateStockForm(forms.ModelForm):
    
    class Meta:
        model = Stock
        exclude=['cant']
