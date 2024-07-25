from django import forms
from apps.products.models import Category

        
class CreateCategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = "__all__"
        
        
        
class UpdateCategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = "__all__"