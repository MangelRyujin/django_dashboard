from django import forms
from apps.products.models import ProductReview

        
class CreateProductReviewForm(forms.ModelForm):
    
    class Meta:
        model = ProductReview
        exclude = ["product","user","is_active"]