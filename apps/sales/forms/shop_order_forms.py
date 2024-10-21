from django import forms
from apps.sales.models import ShopOrder,ShopOrderItem, ShopOrderItemStock
from django.utils.translation import gettext as _

class UpdateShopOrderForm(forms.ModelForm):
    
    class Meta:
        model = ShopOrder
        exclude = ['created_user','state','created_date']
        

class UpdateShopOrderItemForm(forms.ModelForm):
    
    class Meta:
        model = ShopOrderItem
        exclude = ['order','product','price','message']
        

class CreateShopOrderItemStockForm(forms.ModelForm):
    
    class Meta:
        model = ShopOrderItemStock
        exclude = ['item']
        
    def clean_cant(self):
        
        cant = self.cleaned_data.get("cant")
        stock = self.cleaned_data.get("stock")
        if cant <= 0:
                raise forms.ValidationError(_("La cantidad debe de ser mayor que 0"))
        if cant > stock.cant:
                raise forms.ValidationError(_(f"La cantidad debe de ser menor o igual a {stock.cant}"))
        return cant
    
