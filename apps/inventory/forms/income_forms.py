from django import forms
from apps.inventory.models import Income

        
class CreateIncomeForm(forms.ModelForm):
    
    class Meta:
        model = Income
        exclude = ["created_user","created_date"]

class UpdateIncomeForm(forms.ModelForm):
    
    class Meta:
        model = Income
        exclude = ["created_user","created_date"]
