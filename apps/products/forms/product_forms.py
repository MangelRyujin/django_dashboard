from django import forms
from apps.products.models import Product

        
class CreateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"
        
        
        
class UpdateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        exclude =['stock']