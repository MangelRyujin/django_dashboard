from django.shortcuts import redirect, render
from apps.general.models import *
from apps.shop.cart import Cart
from apps.products.models import Product
from django.contrib.auth.decorators import login_required

def shop_cart_view(request):
    cart = Cart(request)
    context = {
        "cart":cart,
        "whatsapp":WhatsAppContact.objects.first(),
        "social":SocialMedia.objects.first(),
        'get_total_items':cart.get_total_items(),
    }
    response= render(request,'shop_templates/productCart/cart.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def cart_add_product(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    if request.POST:
        cart.add_cart(product,int(request.POST.get('cant') or 0))
    context = {
        'get_price_product':cart.get_price_product(product),
        'get_message_product':cart.get_message_product(product),
        'get_cant_product':cart.get_cant_product(product),
        "cart":cart,
        'item_in_cart':cart.item_in_cart(product),
        "product":product,
    }
    response= render(request,'shop_templates/productCart/product_cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def cart_message_product(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    if request.POST:
        cart.add_message_product(product,request.POST.get('message') or None)
    context = {
        'get_price_product':cart.get_price_product(product),
        'get_message_product':cart.get_message_product(product),
        'get_cant_product':cart.get_cant_product(product),
        "cart":cart,
        'item_in_cart':cart.item_in_cart(product),
        "product":product,
    }
    response= render(request,'shop_templates/productCart/product_cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


def cart_remove_product(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    cart.remove(product)
    context = {
        'get_price_product':cart.get_price_product(product),
        # 'get_message_product':cart.get_message_product(product),
        'get_cant_product':cart.get_cant_product(product),
        "cart":cart,
        'item_in_cart':cart.item_in_cart(product),
        "product":product,
    }
    response= render(request,'shop_templates/productCart/product_cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def cart_increment_product(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    cart.increment(product)
    context = {
        'get_price_product':cart.get_price_product(product),
        'get_message_product':cart.get_message_product(product),
        'get_cant_product':cart.get_cant_product(product),
        "cart":cart,
        'item_in_cart':cart.item_in_cart(product),
        "product":product,
    }
    response= render(request,'shop_templates/productCart/product_cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

def cart_decrement_product(request,pk):
    product = Product.objects.filter(pk=pk).first()
    cart = Cart(request)
    cart.decrement(product)
    context = {
        'get_message_product':cart.get_message_product(product),
        'get_price_product':cart.get_price_product(product),
        'get_cant_product':cart.get_cant_product(product),
        "cart":cart,
        'item_in_cart':cart.item_in_cart(product),
        "product":product,
    }
    response= render(request,'shop_templates/productCart/product_cart_update.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

@login_required(login_url='/login/')
def cart_check_view(request):
    cart = Cart(request)
    if cart.get_total_items(): 
        context = {
            "cart":cart,
            "whatsapp":WhatsAppContact.objects.first(),
            "social":SocialMedia.objects.first(),
        }
        if request.POST:
            cart.create_shop_order(request.POST)
            context['cart']={}
            return render(request,'shop_templates/productCart/cart_check_confirm.html',context)
        response= render(request,'shop_templates/productCart/cart_check.html',context)
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response
    return redirect('/')


@login_required(login_url='/login/')
def cart_icon_detail(request):
    cart = Cart(request)
    shop=ShopSales.objects.first()
    context={}
    if shop.is_active:
        cart.clear_items()
        context['cart']=cart
    context['shop']=shop
    return render(request,'shop_templates/productCart/cart_icon.html',context)