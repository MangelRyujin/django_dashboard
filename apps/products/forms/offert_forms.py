from django import forms
from apps.products.models import Offert

        
class CreateOffertForm(forms.ModelForm):
    
    class Meta:
        model = Offert
        fields = "__all__"
        
        
        
class UpdateOffertForm(forms.ModelForm):
    
    class Meta:
        model = Offert
        fields = "__all__"