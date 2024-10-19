from django.shortcuts import render
from apps.general.models import *
from apps.shop.cart import Cart
from apps.products.models import Product


def cart_add_view(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
   
    if request.POST:
        cart.add_cart(product,int(request.POST.get('cant') or 0))
    context = {
        "cart":cart,
        'get_total_items':cart.get_total_items(),
    }
    response= render(request,'shop_templates/productCart/cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def cart_message_view(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    if request.POST:
        cart.add_message_product(product,request.POST.get('message') or None)
    context = {
        "cart":cart,
        'get_total_items':cart.get_total_items(),
    }
    response= render(request,'shop_templates/productCart/cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


def cart_remove_view(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    cart.remove(product)
    context = {
        "cart":cart,
        'get_total_items':cart.get_total_items(),
    }
    response= render(request,'shop_templates/productCart/cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def cart_increment_view(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    cart.increment(product)
    context = {
         "cart":cart,

        'get_total_items':cart.get_total_items(),
    }
    response= render(request,'shop_templates/productCart/cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def cart_decrement_view(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    cart.decrement(product)
    context = {
        "cart":cart,
        'get_total_items':cart.get_total_items(),
    }
    response= render(request,'shop_templates/productCart/cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response