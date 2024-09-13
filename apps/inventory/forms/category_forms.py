from django import forms
from apps.inventory.models import CategoryStock

        
class CreateCategoryStockForm(forms.ModelForm):
    
    class Meta:
        model = CategoryStock
        fields = "__all__"

class UpdateCategoryStockForm(forms.ModelForm):
    
    class Meta:
        model = CategoryStock
        fields = "__all__"
