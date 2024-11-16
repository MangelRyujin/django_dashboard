from django.shortcuts import render
from apps.accounts.decorators import group_required
from apps.inventory.filters import StockFilter, StockMovementFilter
from apps.inventory.forms.stock_forms import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging
from django.contrib.admin.views.decorators import staff_member_required
from apps.inventory.forms.stock_movement_forms import CreateStockMovementMultipleForm, CreateStockMovementSimpleForm
from apps.inventory.models import Stock,CategoryStock, StockMovements,Warehouse
from apps.products.models import Product
logger = logging.getLogger(__name__)

# Stock view (index)
@group_required('administrador')
@staff_member_required(login_url='/')
def stock_movements_view(request):
    response= render(request,'stock_movements_templates/stock_movements.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def stock_movements_table_results(request):
    return  render(request,'stock_movements_templates/stock_movements_table_results.html',context=_show_stock_movements(request))
       
# Stock create form
@staff_member_required(login_url='/')
def stock_movements_simple_create(request):
    context={
         'stocks':Stock.objects.all(),
    }
    
    if request.method == "POST":
        form = CreateStockMovementSimpleForm(request.POST)
        if form.is_valid():
            stock_movement=form.save(commit=False)  
            stock_movement.user = request.user
            stock_movement.movement_type='1'
            if stock_movement.type =='1':
                stock_movement.stock_one.cant-=stock_movement.cant
                
            else:
                stock_movement.stock_one.cant+=stock_movement.cant
            stock_movement.stock_one.save()
            stock_movement.save()
            context['message']='Creado correctamente'
        else:
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'stock_movements_templates/actions/stockCreate/stockMovementSimpleCreateForm.html',context) 
    form = CreateStockMovementSimpleForm()
    context['form']=form
    return render(request,'stock_movements_templates/actions/stockCreate/stockMovementSimpleCreateForm.html',context) 

# Stock create form
@staff_member_required(login_url='/')
def stock_movements_multiple_create(request):
    context={
        'stocks':Stock.objects.all(),
        
    }
    
    if request.method == "POST":
        form = CreateStockMovementMultipleForm(request.POST)
        if form.is_valid():
            stock_movement=form.save(commit=False)   
            stock_movement.user = request.user
            stock_movement.movement_type='2'
            stock_movement.stock_one.cant-=stock_movement.cant
            stock_movement.stock_two.cant+=stock_movement.cant
            stock_movement.stock_one.save()
            stock_movement.stock_two.save()
            stock_movement.save()
            context['message']='Creado correctamente'
        else:
            form_data = request.POST.copy()
            form = CreateStockMovementMultipleForm(form_data)
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'stock_movements_templates/actions/stockCreate/stockMovementMultipleCreateForm.html',context) 
    form = CreateStockMovementMultipleForm()
    context['form']=form
    return render(request,'stock_movements_templates/actions/stockCreate/stockMovementMultipleCreateForm.html',context) 



# Show stock table
@staff_member_required(login_url='/')
def _show_stock_movements(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    stocks_movements = StockMovementFilter(request.GET, queryset=StockMovements.objects.all().order_by('-id'))
    paginator = Paginator(stocks_movements.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail stock table
@staff_member_required(login_url='/')
def stock_movements_detail(request,pk):
    stock_movement = StockMovements.objects.filter(pk=pk).first()
    return  render(request,'stock_movements_templates/actions/stockDetail/stockDetail.html',{"stock_movement":stock_movement})
     