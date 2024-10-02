from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
import logging
from django.core.paginator import Paginator
from apps.sales.filters import LocalOrderFilter
from apps.sales.forms.local_order_forms import CreateLocalOrderForm
from apps.sales.models import LocalOrder
logger = logging.getLogger(__name__)
from django.db.models import Q
  
# Sales demo
@staff_member_required(login_url='/')
def local_order_view(request):
    response= render(request,'sales/local_order_templates/local_order.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response



# Charge result table
@staff_member_required(login_url='/')
def local_order_results_view(request):
    return  render(request,'sales/local_order_templates/local_order_result.html',context=_show_local_order(request))
       
# # Product create form
@staff_member_required(login_url='/')
def local_order_create(request):
    context={}
    if request.method == "POST":
        form = CreateLocalOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_create = request.user
            order.save()
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
        context['form']=form
        return render(request,'sales/local_order_templates/actions/localOrderCreate/localOrderCreateForm.html',context) 
    form = CreateLocalOrderForm()
    context['form']=form
    return render(request,'sales/local_order_templates/actions/localOrderCreate/localOrderCreateForm.html',context) 


# # Product update forms
# @staff_member_required(login_url='/')
# def product_update(request,pk):
#     product = Product.objects.filter(pk=pk).first()
#     form = UpdateProductForm(instance=product)
#     context={}
#     context['product']=product
#     context['form']=form
#     return render(request,'product_templates/actions/productUpdate/productUpdateForm.html',context) 

# # Product main information update form
# @staff_member_required(login_url='/')
# def product_form_update(request,pk):
#     context={}
#     if request.method == "POST":
#         product = Product.objects.filter(pk=pk).first()
#         form = UpdateProductForm(request.POST,request.FILES,instance=product)
#         if form.is_valid():
#             product_form_valid=form.save(commit=False)
#             product_form_valid._change_reason = f'Modifying product {product.name}'
#             product_form_valid.save()
#             form.save_m2m()
#             message="Change product successfully"
#             context['message']=message
#         else:
#             message="Correct the errors"
#             context['error']=message
#         context['product']=product
#         context['form']=form
#         return render(request,'product_templates/actions/productUpdate/productUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def local_order_delete(request,pk):
    local_order = LocalOrder.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if local_order:
            local_order_id=local_order.id
            local_order.delete()
            context = _show_local_order(request)
            context['message']=f'Order {local_order_id} has been delete'
        else:
            context['error']=f'Sorry, product not found'
        return render(request,'sales/local_order_templates/local_order_result.html',context)
    return  render(request,'sales/local_order_templates/actions/localOrderDelete/localOrderDeleteVerify.html',{"local_order":local_order})
     


# Show Product table
@staff_member_required(login_url='/')
def _show_local_order(request):
    keyword = request.session.get('keyword', '')
    
    if request.method == 'POST':
        print("llego post")
        keyword = request.POST.get("keyword",'')
        request.session['keyword'] = keyword
        
    local_orders = LocalOrder.objects.filter(
        Q(pk__icontains=keyword) | Q(user_ci__icontains=keyword)
        | Q(user_last_name__icontains=keyword)| Q(user_phone__icontains=keyword)
        | Q(address__icontains=keyword)| Q(user_first_name__icontains=keyword)
        | Q(localorderitem__product__name__icontains=keyword) | Q(localorderitem__product__code__icontains=keyword)
        ).order_by('-id')
    paginator = Paginator(local_orders, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        'keyword':keyword,
        'pagination':page_obj,
    }
    return context


# Update result table
@staff_member_required(login_url='/')
def local_order_check(request,pk):
    local_order = LocalOrder.objects.filter(pk=pk).first()
    context={"local_order":local_order}
    if local_order:
            local_order.state = "c"
            local_order.save()
            # context['message']=f'There is no sufficient existence'
    else:
            context['error']=f'Sorry, review not found'
    return render(request,'sales/local_order_templates/actions/localOrderCardDetail/localOrderCardDetail.html',context)

# # Detail user Product table
# @staff_member_required(login_url='/')
# def product_detail(request,pk):
#     product = Product.objects.filter(pk=pk).first()
#     return  render(request,'product_templates/actions/productDetail/productDetail.html',{"product":product})
     