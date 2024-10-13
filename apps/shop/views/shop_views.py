from django.shortcuts import render
from apps.general.models import *
from apps.products.models import Product
from utils.funtions.products.product import search_all_products, categories_list_slider, cheap_products, favorite_products, offerts_actives



def shop_view(request):
    context = {
        "whatsapp":WhatsAppContact.objects.first(),
        "social":SocialMedia.objects.first(),
        "offerts":offerts_actives(),
        "hero":PrincipalHeader.objects.first(),
        "categories":categories_list_slider(),
        "favorite_products":favorite_products(request.user),
        "cheap_products":cheap_products(request.user),
    }
    response= render(request,'shop_templates/shop.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def search_product(request):
    return render(request,'shop_templates/landingPage/filters/search.html',search_all_products(request))

def product_like(request,pk):
    product = Product.objects.filter(pk=pk).first()
    if product:
        if product.user_has_like(request.user.id):
            product.likes.remove(request.user)
            like=False
        else:
            product.likes.add(request.user)
            like=True
            
    context={
        "product":{
            "product":product,
            "like": like or False
        }
    }
    return render(request,'shop_templates/landingPage/productsList/productCardEdit.html',context)

def product_cheap_like(request,pk):
    product = Product.objects.filter(pk=pk).first()
    if product:
        if product.user_has_like(request.user.id):
            product.likes.remove(request.user)
            like=False
        else:
            product.likes.add(request.user)
            like=True
            
    context={
        "product":{
            "product":product,
            "like": like or False
        }
    }
    return render(request,'shop_templates/landingPage/productsList/productCardEditCheap.html',context)