from django.shortcuts import render
from apps.products.filters import ProductFilter
from apps.products.forms.product_forms import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging

from apps.products.models import ProductReview
logger = logging.getLogger(__name__)

# Product view (index)
@login_required(login_url='/login/')
def product_review_view(request):
    products = Product.objects.all()
    product_reviews = ProductReview.objects.all()
    response= render(request,'review_templates/review.html',{'product_reviews':product_reviews,'products':products})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response