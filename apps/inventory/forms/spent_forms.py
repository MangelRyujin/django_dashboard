from django import forms
from apps.inventory.models import Spent

        
class CreateSpentForm(forms.ModelForm):
    
    class Meta:
        model = Spent
        exclude = ["created_user","created_date"]

class UpdateSpentForm(forms.ModelForm):
    
    class Meta:
        model = Spent
        exclude = ["created_user","created_date"]
