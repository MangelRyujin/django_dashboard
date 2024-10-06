from django import forms
from apps.sales.models import Order
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from decimal import Decimal

class CreateOrderSoldForm(forms.ModelForm):
    total_paid = forms.DecimalField()
    
    class Meta:
        model = Order
        fields = ['payment_type','cash','transfer','total_paid']
        
    def clean(self):
        cleaned_data = super().clean()
        payment_type = cleaned_data.get('payment_type')
        cash = cleaned_data.get('cash')
        transfer = cleaned_data.get('transfer')
        total_paid = cleaned_data.get('total_paid')
        
        if payment_type == 'c':
            if cash != total_paid:
                raise ValidationError(f"La cantidad de efectivo debe de ser {total_paid}")
            if transfer != 0:
                raise ValidationError(f"la transferencia debe de ser 0")
        elif payment_type == 't':
            if transfer != total_paid:
                raise ValidationError(f"La cantidad de transferencia debe de ser {total_paid}")
            if cash != 0:
                raise ValidationError(f"El efectivo debe de ser 0")
        elif payment_type == 'b':
            if cash <= 0 or transfer <= 0:
                raise ValidationError("Las cantidades a pagar en transferencia y efectivo deben de ser mayores a 0")
            # Verificar si la suma de cash y transfer es igual al total_amount
            if cash + transfer != total_paid:
                raise ValidationError(f"La suma debe de ser igual al total a pagar")
        return cleaned_data