from django.shortcuts import render
from apps.inventory.filters import WarehouseFilter
from apps.inventory.forms.warehouse_forms import CreateWarehouseForm, UpdateWarehouseForm
from apps.inventory.models import Warehouse
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required

# category view (index)
@staff_member_required(login_url='/')
def warehouse_view(request):
    response= render(request,'warehouse_templates/warehouse.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def warehouse_table_results(request):
    return  render(request,'warehouse_templates/warehouse_table_results.html',context=_show_warehouse(request))
       
# category create form
@staff_member_required(login_url='/')
def warehouse_create(request):
    context={}
    if request.method == "POST":
        form = CreateWarehouseForm(request.POST)
        if form.is_valid():
            form.save()  
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
        context['form']=form
        return render(request,'warehouse_templates/actions/warehouseCreate/warehouseCreateForm.html',context) 
    form = CreateWarehouseForm()
    context['form']=form
    return render(request,'warehouse_templates/actions/warehouseCreate/warehouseCreateForm.html',context) 


# category update forms
@staff_member_required(login_url='/')
def warehouse_update(request,pk):
    warehouse = Warehouse.objects.filter(pk=pk).first()
    form = UpdateWarehouseForm(instance=warehouse)
    context={}
    context['warehouse']=warehouse
    context['form']=form
    return render(request,'warehouse_templates/actions/warehouseUpdate/warehouseUpdateForm.html',context) 

# warehouse main information update form
@staff_member_required(login_url='/')
def warehouse_form_update(request,pk):
    context={}
    if request.method == "POST":
        warehouse = Warehouse.objects.filter(pk=pk).first()
        form = UpdateWarehouseForm(request.POST,request.FILES,instance=warehouse)
        if form.is_valid():
            warehouse_form_valid=form.save(commit=False)
            warehouse_form_valid._change_reason = f'Modifying warehouse {warehouse.name}'
            warehouse_form_valid.save()
            message="Change warehouse successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['warehouse']=warehouse
        context['form']=form
        return render(request,'warehouse_templates/actions/warehouseUpdate/warehouseUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def warehouse_delete(request,pk):
    warehouse = Warehouse.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if warehouse:
            warehouse_name=warehouse.name
            warehouse.delete()
            context = _show_warehouse(request)
            context['message']=f'Warehouse {warehouse_name} has been delete'
        else:
            context['error']=f'Sorry, warehouse not found'
        return render(request,'warehouse_templates/warehouse_table_results.html',context)
    return  render(request,'warehouse_templates/actions/warehouseDelete/warehouseDeleteVerify.html',{"warehouse":warehouse})
     


# Show warehouse table
@staff_member_required(login_url='/')
def _show_warehouse(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    warehouses = WarehouseFilter(request.GET, queryset=Warehouse.objects.all().order_by('-id'))
    paginator = Paginator(warehouses.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context
