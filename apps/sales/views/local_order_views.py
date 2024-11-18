from decimal import Decimal
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
import logging
from django.core.paginator import Paginator
from apps.accounts.decorators import group_required
from apps.general.models import LocalSales
from apps.inventory.models import Stock
from apps.products.models import Product
from apps.sales.forms.local_order_forms import CreateLocalOrderForm, CreateLocalOrderItemForm, CreateLocalOrderItemStockForm, UpdateLocalOrderForm, UpdateLocalOrderItemDiscountForm
from apps.sales.forms.order_forms import CreateOrderSoldForm
from apps.sales.models import LocalOrder, LocalOrderItem, LocalOrderItemStock
from apps.sales.utils.local_order import items_discount_or_revert, order_paid_method, order_paid_proccess_data
logger = logging.getLogger(__name__)
from django.db.models import Q
from django.utils.translation import gettext as _
  
# Sales demo
@group_required('administrador','vendedor local')
@staff_member_required(login_url='/')
def local_order_view(request):
    context = {'local':LocalSales.objects.first()}
    response= render(request,'sales/local_order_templates/local_order.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response



# Charge result local orders
@staff_member_required(login_url='/')
def local_order_results_view(request):
    return  render(request,'sales/local_order_templates/local_order_result.html',context=_show_local_order(request))
       
# Local order create form
@staff_member_required(login_url='/')
def local_order_create(request):
    context={}
    if request.method == "POST":
        form = CreateLocalOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_create = request.user
            order.save()
            context['message']='Cración correcta'
        else:
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'sales/local_order_templates/actions/localOrderCreate/localOrderCreateForm.html',context) 
    form = CreateLocalOrderForm()
    context['form']=form
    return render(request,'sales/local_order_templates/actions/localOrderCreate/localOrderCreateForm.html',context) 

# Local order item create form
@staff_member_required(login_url='/')
def local_order_item_create(request,pk):
    local_order=LocalOrder.objects.filter(pk=pk).first()
    context={
       'local_order':local_order,
    }
    context['products'] = [product for product in Product.objects.filter(is_active=True) if product.total_stock > 0 and not local_order.localorderitem_set.filter(product=product) ] 
    if local_order:
        if request.method == "POST":
            form = CreateLocalOrderItemForm(request.POST)
            if form.is_valid():
                order_item = form.save(commit=False)
                order_item.order = local_order
                order_item.save()
                context['products'].remove(order_item.product)
                context['message']='Cración correcta'
            else:
                print(form)
                context['error']='Corrige los errores'
            context['form']=form
            return render(request,'sales/local_order_templates/actions/localOrderItemCreate/localOrderItemCreateForm.html',context) 
    form = CreateLocalOrderItemForm()
    context['form']=form
    return render(request,'sales/local_order_templates/actions/localOrderItemCreate/localOrderItemCreateForm.html',context) 

# Local order item stock create form
@staff_member_required(login_url='/')
def local_order_item_stock_create(request,pk):
    local_order_item = LocalOrderItem.objects.filter(pk=pk).first()
    context={
       'local_order_item':local_order_item,
    }
    context['stocks'] = [stock for stock in Stock.objects.filter(is_active=True,cant__gt=0,product=local_order_item.product) if not local_order_item.localorderitemstock_set.filter(stock=stock) ] 
   
    if local_order_item:
        if request.method == "POST":
            form = CreateLocalOrderItemStockForm(request.POST)
            if form.is_valid():
                local_order_item_stock = form.save(commit=False)
                local_order_item_stock.item = local_order_item
                local_order_item_stock.save()
                context['stocks'].remove(local_order_item_stock.stock)
                context['message']='Cración correcta'
            else:
                context['error']='Corrige los errores'
            
            context['form']=form
            return render(request,'sales/local_order_templates/actions/localOrderItemStockCreate/localOrderItemStockCreateForm.html',context) 
    form = CreateLocalOrderItemStockForm()
    context['form']=form
    return render(request,'sales/local_order_templates/actions/localOrderItemStockCreate/localOrderItemStockCreateForm.html',context) 


# # Local order update forms
@staff_member_required(login_url='/')
def local_order_update(request,pk):
    local_order = LocalOrder.objects.filter(pk=pk).first()
    form = UpdateLocalOrderForm(instance=local_order)
    context={}
    context['local_order']=local_order
    context['form']=form
    return render(request,'sales/local_order_templates/actions/localOrderUpdate/localOrderUpdateForm.html',context) 

# # Product main information update form
@staff_member_required(login_url='/')
def local_order_form_update(request,pk):
    context={}
    if request.method == "POST":
        local_order = LocalOrder.objects.filter(pk=pk).first()
        form = UpdateLocalOrderForm(request.POST,instance=local_order)
        if form.is_valid():
            form.save()
            message="Edición correcta"
            context['message']=message
        else:
            message="Corrige los errores"
            context['error']=message
        context['local_order']=local_order
        context['form']=form
        return render(request,'sales/local_order_templates/actions/localOrderUpdate/localOrderUpdateCheckForm.html',context) 


# Delete local order
@staff_member_required(login_url='/')
def local_order_delete(request,pk):
    local_order = LocalOrder.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if local_order:
            if local_order.state == 'c':
                items_discount_or_revert(local_order,'revert')
            local_order_id=local_order.id
            local_order.delete()
            context = _show_local_order(request)
            context['message']=f'Orden {local_order_id} ha sido eliminada'
        else:
            context['error']=f'Lo sentimos, la orden no existe'
        return render(request,'sales/local_order_templates/local_order_result.html',context)
    return  render(request,'sales/local_order_templates/actions/localOrderDelete/localOrderDeleteVerify.html',{"local_order":local_order})

# Delete local order item
@staff_member_required(login_url='/')
def local_order_item_delete(request,pk):
    local_order_item = LocalOrderItem.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if local_order_item:
            local_order = LocalOrder.objects.filter(pk=local_order_item.order.pk).first()
            context['local_order']=local_order
            local_order_item.delete()
    return render(request,'sales/local_order_templates/actions/localOrderCardDetail/localOrderCardDetail.html',context)


# Add discount to local order item
@staff_member_required(login_url='/')
def local_order_item_discount(request,pk):
    local_order_item = LocalOrderItem.objects.filter(pk=pk).first()
    form=UpdateLocalOrderItemDiscountForm(instance=local_order_item)
    context={}
    if request.method == "POST":
        form=UpdateLocalOrderItemDiscountForm(request.POST,instance=local_order_item)
        if form.is_valid():
            form.save()
            context['message']="Descuento aplicado con éxito"
            
    context["local_order_item"]=local_order_item
    context['form']=form
    return render(request,'sales/local_order_templates/actions/localOrderItemDiscount/localOrderItemDiscountVerify.html',context)

# Delete local order item stock
@staff_member_required(login_url='/')
def local_order_item_stock_delete(request,pk):
    local_order_item_stock = LocalOrderItemStock.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if local_order_item_stock:
            local_order = LocalOrder.objects.filter(pk=local_order_item_stock.item.order.pk).first()
            context['local_order']=local_order
            local_order_item_stock.delete()
    return render(request,'sales/local_order_templates/actions/localOrderCardDetail/localOrderCardDetail.html',context)

# Show local orders list
@staff_member_required(login_url='/')
def _show_local_order(request):
    keyword = request.session.get('keyword', '')
    
    if request.method == 'POST':
        keyword = request.POST.get("keyword",'')
        request.session['keyword'] = keyword
        
    local_orders = LocalOrder.objects.filter(
        Q(pk__icontains=keyword) | Q(user_ci__icontains=keyword)
        | Q(user_last_name__icontains=keyword)| Q(user_phone__icontains=keyword)
        | Q(address__icontains=keyword)| Q(user_first_name__icontains=keyword)
        | Q(localorderitem__product__name__icontains=keyword) | Q(localorderitem__product__code__icontains=keyword)
        ).distinct().order_by('-id')
    paginator = Paginator(local_orders, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        'keyword':keyword,
        'pagination':page_obj,
    }
    return context


# Local order checked
@staff_member_required(login_url='/')
def local_order_check_revert(request,pk):
    local_order = LocalOrder.objects.filter(pk=pk).first()
    context={"local_order":local_order}
    if local_order:
        if local_order.state == 'p':
            if local_order.items_exists():
                items_discount_or_revert(local_order,'discount')
                local_order.state = "c"
                local_order.save()  
            else:
                context['message']=f'No contiene suficiente existencia'
        else:
            items_discount_or_revert(local_order,'revert')
            local_order.state = "p"
            local_order.save() 
    else:
        context['error']=f'Lo sentimos, la orden no existe'
    return render(request,'sales/local_order_templates/actions/localOrderCardDetail/localOrderCardDetail.html',context)

# # Detail local order
@staff_member_required(login_url='/')
def local_order_detail(request,pk):
    local_order = LocalOrder.objects.filter(pk=pk).first()
    return  render(request,'sales/local_order_templates/actions/localOrderCardDetail/localOrderCardDetail.html',{"local_order":local_order})
     
     
# # Detail local order
@staff_member_required(login_url='/')
def local_order_sold(request,pk):
    local_order = LocalOrder.objects.filter(pk=pk).first()
    context={
        "local_order":local_order
    }
    if request.method == "POST":
        data = order_paid_proccess_data(request.POST,local_order.total_price)
        form = CreateOrderSoldForm(data)
        if form.is_valid():
            order_paid_method(local_order,data["payment_type"],data['cash'],data['transfer'])
            context["message"]=_("Pago realizado")
        else:
            context["form"]=form
    return render(request,'sales/local_order_templates/actions/localOrderSold/localOrderSoldVerify.html',context)
      
# Delete local order
@staff_member_required(login_url='/')
def local_order_delete_sold(request,pk):
    local_order = LocalOrder.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if local_order:
            local_order_id=local_order.id
            local_order.delete()
            context = _show_local_order(request)
            context['message']=f'Orden {local_order_id} ha sido pagada'
        else:
            context['error']=f'Lo sentimos, la orden no existe'
        return render(request,'sales/local_order_templates/local_order_result.html',context)