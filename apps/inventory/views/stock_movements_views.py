from django.shortcuts import render
from apps.inventory.filters import StockFilter
from apps.inventory.forms.stock_forms import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging

from apps.inventory.models import Stock,CategoryStock,Warehouse
from apps.products.models import Product
logger = logging.getLogger(__name__)

# Stock view (index)
@login_required(login_url='/login/')
def stock_movements_view(request):
    categories = CategoryStock.objects.all()
    warehouses = Warehouse.objects.all()
    products = Product.objects.all()
    response= render(request,'stock_movements_templates/stock_movements.html',{'categories':categories,'warehouses':warehouses,'products': products})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@login_required(login_url='/login/')
def stock_movements_table_results(request):
    return  render(request,'stock_movements_templates/stock_movements_table_results.html',context=_show_stock_movements(request))
       
# Stock create form
@login_required(login_url='/login/')
def stock_movements_create(request):
    context={
        'categories':CategoryStock.objects.all(),
        'warehouses': Warehouse.objects.all(),
        'products': Product.objects.all()
    }
    
    if request.method == "POST":
        form = CreateStockForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
        context['form']=form
        return render(request,'stock_templates/actions/stockCreate/stockCreateForm.html',context) 
    form = CreateStockForm()
    context['form']=form
    return render(request,'stock_templates/actions/stockCreate/stockCreateForm.html',context) 


# Stock update forms
@login_required(login_url='/login/')
def  stock_movements_update(request,pk):
    stock = Stock.objects.filter(pk=pk).first()
    form = UpdateStockForm(instance=stock)
    context={}
    context['stock']=stock
    context['form']=form
    return render(request,'stock_templates/actions/stockUpdate/stockUpdateForm.html',context) 

# Stock main information update form
@login_required(login_url='/login/')
def stock_movements_form_update(request,pk):
    context={}
    if request.method == "POST":
        stock = Stock.objects.filter(pk=pk).first()
        form = UpdateStockForm(request.POST,instance=stock)
        if form.is_valid():
            stock_form_valid=form.save(commit=False)
            stock_form_valid._change_reason = f'Modifying stock {stock.name}'
            stock_form_valid.save()
            form.save_m2m()
            message="Change stock successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        print(form)
        context['stock']=stock
        context['form']=form
        return render(request,'stock_templates/actions/stockUpdate/stockUpdateCheckForm.html',context) 


# Delete result table
@login_required(login_url='/login/')
def stock_movements_delete(request,pk):
    stock = Stock.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if stock:
            stock_name=stock.name
            stock.delete()
            context = _show_stock_movements(request)
            context['message']=f'{stock_name} has been delete'
        else:
            context['error']=f'Sorry, stock not found'
        return render(request,'stock_templates/stock_table_results.html',context)
    return  render(request,'stock_templates/actions/stockDelete/stockDeleteVerify.html',{"stock":stock})
     


# Show stock table
def _show_stock_movements(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    stocks = StockFilter(request.GET, queryset=Stock.objects.all().order_by('-id'))
    paginator = Paginator(stocks.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail stock table
@login_required(login_url='/login/')
def stock_movements_detail(request,pk):
    stock = Stock.objects.filter(pk=pk).first()
    return  render(request,'stock_templates/actions/stockDetail/stockDetail.html',{"stock":stock})
     