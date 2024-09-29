from django.shortcuts import render
from apps.general.models import *

def products_store_view(request): 
    response= render(request,'shop_templates/products.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response