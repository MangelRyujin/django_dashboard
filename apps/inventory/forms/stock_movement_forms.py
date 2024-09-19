from django import forms
from apps.inventory.models import  Stock, StockMovements
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
        
class CreateStockMovementMultipleForm(forms.ModelForm):
    
    class Meta:
        model = StockMovements
        exclude=['user','type','movement_type']

        
    def clean_cant(self):
        cant = self.cleaned_data.get("cant")
        if cant <= 0:
                raise forms.ValidationError(_("The quantity cannot be less than 0"))
        return cant

    def clean_stock_one(self):
        stock_one = self.cleaned_data.get("stock_one")
        cant = self.cleaned_data.get("cant")
        if cant:
            if stock_one.cant < cant:
                raise forms.ValidationError(_("The stock does not have enough quantity"))
        return stock_one

        
    def clean_stock_two(self):
        stock_one = self.cleaned_data.get("stock_one")
        stock_two = self.cleaned_data.get("stock_two")
        
        if stock_one == stock_two :
            raise forms.ValidationError(_("Stock one don't equal stock two"))
        return stock_two
    

class CreateStockMovementSimpleForm(forms.ModelForm):
    
    class Meta:
        model = StockMovements
        exclude=['stock_two','user','movement_type']

    def clean_stock_one(self):
        cleaned_data = super().clean()
        stock_one = cleaned_data.get('stock_one')
        cant = cleaned_data.get('cant')
        if cleaned_data.get('type')=='1':
            if cant > stock_one.cant:
                raise ValidationError("The stock does not have enough quantity.")
        return stock_one
    
    def clean_cant(self):
        cleaned_data = super().clean()
        cant = cleaned_data.get('cant')
        if cant <= 0:
                raise forms.ValidationError(_("The quantity cannot be less than 0"))
        return cant
    
    