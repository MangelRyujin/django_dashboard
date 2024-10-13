from django.shortcuts import render
from apps.general.models import *
from apps.products.models import Category, Product
from django.core.paginator import Paginator

def products_store_view(request): 
    context = {
        "whatsapp":WhatsAppContact.objects.first(),
        "social":SocialMedia.objects.first(),
        "categories":Category.objects.filter(is_active=True),
        "products":_show_product(request)
    }
    response= render(request,'shop_templates/products.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Product list filter
def product_list_results(request):
    context = {
        
        "products":_show_product(request)
    }
    return  render(request,'shop_templates/product_filter.html',context)
       


# Show Product 
def _show_product(request):
    get_copy = request.GET.copy()
    category=get_copy.get('categories') or None
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    products=[]
    products_list = Product.objects.filter(is_active=True) if category==None or category=='' else Product.objects.filter(is_active=True,categories=category)
    for product in products_list:
        like=product.user_has_like(request.user.id)
        products.append(
            {
                'like':like,
                'product':product
            }
        )
    paginator = Paginator(products, 24)    # Show 24 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context