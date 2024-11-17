from django import forms
from apps.products.models import PrincipalCategory

        
class CreatePrincipalCategoryForm(forms.ModelForm):
    
    class Meta:
        model = PrincipalCategory
        fields = "__all__"
        
        
        
class UpdatePrincipalCategoryForm(forms.ModelForm):
    
    class Meta:
        model = PrincipalCategory
        fields = "__all__"