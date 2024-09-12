from django.shortcuts import render
from apps.products.filters import ProductReviewFilter
from apps.products.forms.reviews_forms import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging

from apps.products.models import ProductReview,Product,Category
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

@login_required(login_url='/login/')
def product_table_reviews_results(request):
    return  render(request,'review_templates/product_table_reviews_results.html',context=_show_product_reviews(request))

def _show_product_reviews(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    Products = ProductReviewFilter(request.GET, queryset=ProductReview.objects.all().order_by('-id'))
    paginator = Paginator(Products.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context

# Product create form
@login_required(login_url='/login/')
def product_create_reviews(request):
    context={
        'categories':Category.objects.all()
    }
    
    if request.method == "POST":
        form = UpdateProductReviewForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
        context['form']=form
        return render(request,'product_templates/actions/productCreate/productCreateReviewForm.html',context) 
    form = CreateProductReviewForm()
    context['form']=form
    return render(request,'product_templates/actions/productCreate/productCreateReviewForm.html',context) 

# Product update forms
@login_required(login_url='/login/')
def product_update_reviews(request,pk):
    product = Product.objects.filter(pk=pk).first()
    form = UpdateProductReviewForm(instance=product)
    context={}
    context['product']=product
    context['form']=form
    return render(request,'product_templates/actions/productUpdate/productUpdateForm.html',context) 

# Product main information update form
@login_required(login_url='/login/')
def product_form_update_reviews(request,pk):
    context={}
    if request.method == "POST":
        product = Product.objects.filter(pk=pk).first()
        form = UpdateProductReviewForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            product_form_valid=form.save(commit=False)
            product_form_valid._change_reason = f'Modifying product {product.name}'
            product_form_valid.save()
            form.save_m2m()
            message="Change product successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['product']=product
        context['form']=form
        return render(request,'product_templates/actions/productUpdate/productUpdateCheckForm.html',context)

# Delete result table
@login_required(login_url='/login/')
def product_delete_reviews(request,pk):
    product = Product.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if product:
            product_name=product.name
            product.delete()
            context = _show_product_reviews(request)
            context['message']=f'{product_name} has been delete'
        else:
            context['error']=f'Sorry, product not found'
        return render(request,'product_templates/product_table_results.html',context)
    return  render(request,'product_templates/actions/productDelete/productDeleteVerify.html',{"product":product}) 