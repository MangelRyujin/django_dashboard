from django import forms
from apps.products.models import ProductReview

        
class CreateProductReviewForm(forms.ModelForm):
    
    class Meta:
        model = ProductReview
        fields = "__all__"
        
        
        
class UpdateProductReviewForm(forms.ModelForm):
    
    class Meta:
        model = ProductReview
        exclude ="__all__"