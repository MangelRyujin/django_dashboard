from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
import logging
from django.core.paginator import Paginator
from apps.inventory.models import Stock
from apps.sales.forms.order_forms import CreateOrderSoldForm
from apps.sales.forms.shop_order_forms import CreateShopOrderItemStockForm, UpdateShopOrderForm, UpdateShopOrderItemForm
from apps.sales.models import ShopOrder, ShopOrderItem, ShopOrderItemStock
from apps.sales.utils.shop_order import shop_items_discount_or_revert, shop_order_paid_method, shop_order_paid_proccess_data
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
                if shop_order_item_form.stocks_available < 0:
                    shop_order_item_form.shoporderitemstock_set.all().delete()
                context['message']='Edición correcta'
            else:
                context['error']='Corrige los errores'
            context['form']=form
            return render(request,'sales/shop_order_templates/actions/shopOrderItemUpdate/shopOrderItemUpdateForm.html',context) 
    form = UpdateShopOrderItemForm(instance=shop_order_item)
    context['form']=form
    return render(request,'sales/shop_order_templates/actions/shopOrderItemUpdate/shopOrderItemUpdateForm.html',context) 

# shop order item stock create form
@staff_member_required(login_url='/')
def shop_order_item_stock_create(request,pk):
    shop_order_item = ShopOrderItem.objects.filter(pk=pk).first()
    context={
       'shop_order_item':shop_order_item,
    }
    context['stocks'] = [stock for stock in Stock.objects.filter(is_active=True,cant__gt=0,product=shop_order_item.product.pk) if not shop_order_item.shoporderitemstock_set.filter(stock=stock) ] 
   
    if shop_order_item:
        if request.method == "POST":
            form = CreateShopOrderItemStockForm(request.POST)
            if form.is_valid():
                shop_order_item_stock = form.save(commit=False)
                shop_order_item_stock.item = shop_order_item
                shop_order_item_stock.save()
                context['stocks'].remove(shop_order_item_stock.stock)
                context['message']='Creada correctamente'
            else:
                context['error']='Corrige los errores'
            
            context['form']=form
            return render(request,'sales/shop_order_templates/actions/shopOrderItemStockCreate/shopOrderItemStockCreateForm.html',context) 
    form = CreateShopOrderItemStockForm()
    context['form']=form
    return render(request,'sales/shop_order_templates/actions/shopOrderItemStockCreate/shopOrderItemStockCreateForm.html',context) 


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
            message="Edición correcta"
            context['message']=message
        else:
            message="Corrige los errores"
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
                shop_items_discount_or_revert(shop_order,'revert')
            shop_order_id=shop_order.id
            shop_order.delete()
            context = _show_shop_order(request)
            context['message']=f'Orden {shop_order_id} ha sido eliminada'
        else:
            context['error']=f'Lo sentimos, la orden no existe'
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


# Delete shop order item stock
@staff_member_required(login_url='/')
def shop_order_item_stock_delete(request,pk):
    shop_order_item_stock = ShopOrderItemStock.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if shop_order_item_stock:
            shop_order = ShopOrder.objects.filter(pk=shop_order_item_stock.item.order.pk).first()
            context['shop_order']=shop_order
            shop_order_item_stock.delete()
    return render(request,'sales/shop_order_templates/actions/shopOrderCardDetail/shopOrderCardDetail.html',context)

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


# shop order checked
@staff_member_required(login_url='/')
def shop_order_check_revert(request,pk):
    shop_order = ShopOrder.objects.filter(pk=pk).first()
    context={"shop_order":shop_order}
    if shop_order:
        if shop_order.state == 'p':
            if shop_order.items_exists():
                shop_items_discount_or_revert(shop_order,'discount')
                shop_order.state = "c"
                shop_order.save()  
            else:
                context['message']=f'No contienes la existencia suficiente'
        else:
            shop_items_discount_or_revert(shop_order,'revert')
            shop_order.state = "p"
            shop_order.save() 
    else:
        context['error']=f'Lo sentimos, la orden no existe'
    return render(request,'sales/shop_order_templates/actions/shopOrderCardDetail/shopOrderCardDetail.html',context)

# # Detail shop order
@staff_member_required(login_url='/')
def shop_order_detail(request,pk):
    shop_order = ShopOrder.objects.filter(pk=pk).first()
    return  render(request,'sales/shop_order_templates/actions/shopOrderCardDetail/shopOrderCardDetail.html',{"shop_order":shop_order})
     
     
# # Detail shop order
@staff_member_required(login_url='/')
def shop_order_sold(request,pk):
    shop_order = ShopOrder.objects.filter(pk=pk).first()
    context={
        "shop_order":shop_order
    }
    if request.method == "POST":
        data = shop_order_paid_proccess_data(request.POST,shop_order.total_price)
        form = CreateOrderSoldForm(data)
        if form.is_valid():
            shop_order_paid_method(shop_order,data["payment_type"],data['cash'],data['transfer'],request.user)
            context["message"]=_("Pago realizado")
        else:
            context["form"]=form
    return render(request,'sales/shop_order_templates/actions/shopOrderSold/shopOrderSoldVerify.html',context)
      
# Delete local order
@staff_member_required(login_url='/')
def shop_order_delete_sold(request,pk):
    shop_order = ShopOrder.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if shop_order:
            shop_order_id=shop_order.id
            shop_order.delete()
            context = _show_shop_order(request)
            context['message']=f'Orden {shop_order_id} ha sido pagada'
        else:
            context['error']=f'Lo sentimos, la orden no existe'
        return render(request,'sales/shop_order_templates/shop_order_result.html',context)