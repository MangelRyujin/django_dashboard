from django.shortcuts import render
from apps.general.models import *
from apps.shop.forms.reviews_forms import CreateProductReviewForm
from apps.products.models import Product, ProductReview
from utils.funtions.products.product import favorite_products

def shop_product_add_cart_view(request,pk):
    product = Product.objects.filter(pk=pk).first()
    context = {
        "whatsapp":WhatsAppContact.objects.first(),
        "social":SocialMedia.objects.first(),
        "product":product,
    }
    response= render(request,'shop_templates/productCart/product_cart.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response