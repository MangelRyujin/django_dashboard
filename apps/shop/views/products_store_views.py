from django.shortcuts import render
from apps.general.models import *

def products_store_view(request):
    return render(request,'shop_templates/products.html')