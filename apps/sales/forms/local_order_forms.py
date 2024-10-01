from django import forms
from apps.sales.models import LocalOrder

        
class CreateLocalOrderForm(forms.ModelForm):
    
    class Meta:
        model = LocalOrder
        exclude = ['user_create','state','created_date']
        
        
        
class UpdateLocalOrderForm(forms.ModelForm):
    
    class Meta:
        model = LocalOrder
        exclude = ['user_create','state','created_date']