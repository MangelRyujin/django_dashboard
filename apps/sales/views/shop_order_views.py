from decimal import Decimal
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
import logging
from django.core.paginator import Paginator
from apps.inventory.models import Stock
from apps.products.models import Product
from apps.sales.forms.local_order_forms import CreateLocalOrderForm, CreateLocalOrderItemForm, CreateLocalOrderItemStockForm, UpdateLocalOrderForm
from apps.sales.forms.order_forms import CreateOrderSoldForm
from apps.sales.forms.shop_order_forms import UpdateShopOrderForm, UpdateShopOrderItemForm
from apps.sales.models import LocalOrder, LocalOrderItem, LocalOrderItemStock, ShopOrder, ShopOrderItem
from apps.sales.utils.local_order import items_discount_or_revert, order_paid_method, order_paid_proccess_data
logger = logging.getLogger(__name__)
from django.db.models import Q
from django.utils.translation import gettext as _
  
# Sales demo
@staff_member_required(login_url='/')
def shop_order_view(request):
    response= render(request,'sales/shop_order_templates/shop_order.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response



# Charge result shop orders
@staff_member_required(login_url='/')
def shop_order_results_view(request):
    return  render(request,'sales/shop_order_templates/shop_order_result.html',context=_show_shop_order(request))
       
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
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
        context['form']=form
        return render(request,'sales/local_order_templates/actions/localOrderCreate/localOrderCreateForm.html',context) 
    form = CreateLocalOrderForm()
    context['form']=form
    return render(request,'sales/local_order_templates/actions/localOrderCreate/localOrderCreateForm.html',context) 

# shop order item create form
@staff_member_required(login_url='/')
def shop_order_item_update(request,pk):
    shop_order_item=ShopOrderItem.objects.filter(pk=pk).first()
    context={
       'shop_order_item':shop_order_item,
    }
    if shop_order_item:
        if request.method == "POST":
            form = UpdateShopOrderItemForm(request.POST,instance=shop_order_item)
            if form.is_valid():
                shop_order_item_form = form.save(commit=False)
                shop_order_item_form.price = round(shop_order_item.product.total_price * shop_order_item_form.cant,2)
                shop_order_item_form.save()
                context['message']='Update successfully'
            else:
                context['error']='Correct the errors'
            context['form']=form
            return render(request,'sales/shop_order_templates/actions/shopOrderItemUpdate/shopOrderItemUpdateForm.html',context) 
    form = UpdateShopOrderItemForm(instance=shop_order_item)
    context['form']=form
    return render(request,'sales/shop_order_templates/actions/shopOrderItemUpdate/shopOrderItemUpdateForm.html',context) 

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
                context['message']='Created successfully'
            else:
                context['error']='Correct the errors'
            
            context['form']=form
            return render(request,'sales/local_order_templates/actions/localOrderItemStockCreate/localOrderItemStockCreateForm.html',context) 
    form = CreateLocalOrderItemStockForm()
    context['form']=form
    return render(request,'sales/local_order_templates/actions/localOrderItemStockCreate/localOrderItemStockCreateForm.html',context) 


# # shop order update forms
@staff_member_required(login_url='/')
def shop_order_update(request,pk):
    shop_order = ShopOrder.objects.filter(pk=pk).first()
    form = UpdateShopOrderForm(instance=shop_order)
    context={}
    context['shop_order']=shop_order
    context['form']=form
    return render(request,'sales/shop_order_templates/actions/shopOrderUpdate/shopOrderUpdateForm.html',context) 

# # Product main information update form
@staff_member_required(login_url='/')
def shop_order_form_update(request,pk):
    context={}
    if request.method == "POST":
        shop_order = ShopOrder.objects.filter(pk=pk).first()
        form = UpdateShopOrderForm(request.POST,instance=shop_order)
        if form.is_valid():
            form.save()
            message="Change order successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['shop_order']=shop_order
        context['form']=form
        return render(request,'sales/shop_order_templates/actions/shopOrderUpdate/shopOrderUpdateCheckForm.html',context) 


# Delete shop order
@staff_member_required(login_url='/')
def shop_order_delete(request,pk):
    shop_order = ShopOrder.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if shop_order:
            if shop_order.state == 'c':
                items_discount_or_revert(shop_order,'revert')
            shop_order_id=shop_order.id
            shop_order.delete()
            context = _show_shop_order(request)
            context['message']=f'Order {shop_order_id} has been delete'
        else:
            context['error']=f'Sorry, product not found'
        return render(request,'sales/shop_order_templates/shop_order_result.html',context)
    return  render(request,'sales/shop_order_templates/actions/shopOrderDelete/shopOrderDeleteVerify.html',{"shop_order":shop_order})

# Delete shop order item
@staff_member_required(login_url='/')
def shop_order_item_delete(request,pk):
    shop_order_item = ShopOrderItem.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if shop_order_item:
            shop_order = ShopOrder.objects.filter(pk=shop_order_item.order.pk).first()
            context['shop_order']=shop_order
            shop_order_item.delete()
    return render(request,'sales/shop_order_templates/actions/shopOrderCardDetail/shopOrderCardDetail.html',context)


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
def _show_shop_order(request):
    keyword = request.session.get('keyword', '')
    
    if request.method == 'POST':
        keyword = request.POST.get("keyword",'')
        request.session['keyword'] = keyword
        
    shop_orders = ShopOrder.objects.filter(
        Q(pk__icontains=keyword) | Q(created_user__ci__icontains=keyword)
        | Q(created_user__last_name__icontains=keyword)| Q(created_user__phone_number__icontains=keyword)
        | Q(address__icontains=keyword)| Q(created_user__first_name__icontains=keyword)
        | Q(shoporderitem__product__name__icontains=keyword) | Q(shoporderitem__product__code__icontains=keyword)
        ).distinct().order_by('id')
    paginator = Paginator(shop_orders, 25)    # Show 25 contacts per page.
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
                context['message']=f'There is no sufficient existence'
        else:
            items_discount_or_revert(local_order,'revert')
            local_order.state = "p"
            local_order.save() 
    else:
        context['error']=f'Sorry, review not found'
    return render(request,'sales/local_order_templates/actions/localOrderCardDetail/localOrderCardDetail.html',context)

# # Detail shop order
@staff_member_required(login_url='/')
def shop_order_detail(request,pk):
    shop_order = ShopOrder.objects.filter(pk=pk).first()
    return  render(request,'sales/shop_order_templates/actions/shopOrderCardDetail/shopOrderCardDetail.html',{"shop_order":shop_order})
     
     
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
            context["message"]=_("Payment successfully")
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
            context = _show_shop_order(request)
            context['message']=f'Order {local_order_id} has been paid'
        else:
            context['error']=f'Sorry, product not found'
        return render(request,'sales/local_order_templates/local_order_result.html',context)