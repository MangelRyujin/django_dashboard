from django.shortcuts import render
from apps.general.models import *
from apps.shop.cart import Cart
from apps.shop.forms.reviews_forms import CreateProductReviewForm
from apps.products.models import Product, ProductReview
from utils.funtions.products.product import favorite_products

def shop_product_detail_view(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    if product:
      product.views+=1
      product.save()
    context = {
        'get_price_product':cart.get_price_product(product),
        'get_message_product':cart.get_message_product(product),
        'get_cant_product':cart.get_cant_product(product),
        "cart":cart,
        'item_in_cart':cart.item_in_cart(product),
        "whatsapp":WhatsAppContact.objects.first(),
        "social":SocialMedia.objects.first(),
        "product":product,
        "reviews":ProductReview.objects.filter(is_active=True,product=product)[:5],
        "favorite_products":favorite_products(request.user),
        "form":CreateProductReviewForm()
    }
    response= render(request,'shop_templates/productDetail/product_detail.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def create_product_review(request,pk):
    product = Product.objects.filter(pk=pk).first()
    context={"product":product}
    if request.method == "POST":
        form=CreateProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user=request.user
            review.product=product
            review.save()
            context['message']="Reseña enviada con éxito"
        else:
            context['error']=form.errors
    context['form']=form        
    return render(request,'shop_templates/productDetail/reviews/reviewModalResponse.html',context)