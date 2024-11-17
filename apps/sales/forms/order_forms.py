from django import forms
from apps.sales.models import Order
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from decimal import Decimal

class CreateOrderSoldForm(forms.ModelForm):
    total_paid = forms.DecimalField()
    total_price = forms.DecimalField()
    
    class Meta:
        model = Order
        fields = ['payment_type','cash','transfer','total_paid','total_price']
        
    def clean(self):
        cleaned_data = super().clean()
        total_paid = cleaned_data.get('total_paid')
        total_price = cleaned_data.get('total_price')

        if total_paid != total_price:
            raise ValidationError(_(f"El total a pagar tiene que ser igual a {total_paid}."))