from django import forms
from apps.general.models import LocalSales, PrincipalHeader, ShopSales,SocialMedia,WhatsAppContact

        
class UpdatePrincipalHeaderForm(forms.ModelForm):
    
    class Meta:
        model = PrincipalHeader
        fields = "__all__"
        

class UpdateSocialMediaForm(forms.ModelForm):
    
    class Meta:
        model = SocialMedia
        fields = "__all__"
        

class UpdateWhatsAppContactForm(forms.ModelForm):
    
    class Meta:
        model = WhatsAppContact
        fields = "__all__"
        
        
class UpdateLocalSalesForm(forms.ModelForm):
    
    class Meta:
        model = LocalSales
        fields = "__all__"
        

class UpdateShopSalesForm(forms.ModelForm):
    
    class Meta:
        model = ShopSales
        fields = "__all__"
        