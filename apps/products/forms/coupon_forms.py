from django import forms
from apps.products.models import Coupon

        
class CreateCouponForm(forms.ModelForm):
    
    class Meta:
        model = Coupon
        exclude = ["code","is_exhausted","is_active"]
        
        
        
class UpdateCouponForm(forms.ModelForm):
    
    class Meta:
        model = Coupon
        exclude = ["code","is_exhausted",]