from django import forms
from apps.sales.models import ShopOrder,ShopOrderItem
from django.utils.translation import gettext as _

class UpdateShopOrderForm(forms.ModelForm):
    
    class Meta:
        model = ShopOrder
        exclude = ['created_user','state','created_date']
        

class UpdateShopOrderItemForm(forms.ModelForm):
    
    class Meta:
        model = ShopOrderItem
        exclude = ['order','product','price','message']
        
