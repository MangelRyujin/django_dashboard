from django import forms
from apps.sales.models import LocalOrder,LocalOrderItem, LocalOrderItemStock
from django.utils.translation import gettext as _
        
class CreateLocalOrderForm(forms.ModelForm):
    
    class Meta:
        model = LocalOrder
        exclude = ['user_create','state','created_date']
        

        
class UpdateLocalOrderForm(forms.ModelForm):
    
    class Meta:
        model = LocalOrder
        exclude = ['user_create','state','created_date']
        
class UpdateLocalOrderItemDiscountForm(forms.ModelForm):
    class Meta:
        model = LocalOrderItem
        exclude = ['order','product']

class CreateLocalOrderItemForm(forms.ModelForm):
    
    class Meta:
        model = LocalOrderItem
        exclude = ['order','discount']
        
        
class CreateLocalOrderItemStockForm(forms.ModelForm):
    
    class Meta:
        model = LocalOrderItemStock
        exclude = ['item']
        
    def clean_cant(self):
        cant = self.cleaned_data.get("cant")
        stock = self.cleaned_data.get("stock")
        if cant <= 0:
                raise forms.ValidationError(_("La cantidad debe de ser mayor que 0"))
        if cant > stock.cant:
                raise forms.ValidationError(_(f"La cantidad debe de ser menor o igual a {stock.cant}"))
        return cant
    
