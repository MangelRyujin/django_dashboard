from django import forms
from apps.sales.models import Shift
from django.utils.translation import gettext as _

class CreateShiftForm(forms.ModelForm):

    class Meta:
        model = Shift
        fields = ['warehouse']
        
class UpdateShiftForm(forms.ModelForm):

    class Meta:
        model = Shift
        fields = ['warehouse']