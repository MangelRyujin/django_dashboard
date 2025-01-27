from django.shortcuts import render,get_object_or_404,redirect
from apps.accounts.decorators import group_required
from apps.inventory.filters import CategoryStockFilter
from apps.inventory.models import CategoryStock, Warehouse
from apps.products.forms.category_forms import *
from django.core.paginator import Paginator
import logging
from apps.sales.filters import ShiftFilter
from apps.sales.forms.shift_forms import CreateShiftForm, UpdateShiftForm
from apps.sales.models import Shift
from apps.sales.utils.products_shift import closed_shift, create_product_shfit
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required

# shift view (index)
@staff_member_required(login_url='/')
def shift_view(request):
    context={
        "form" : CreateShiftForm(),
        "warehouses":Warehouse.objects.all()
    }
    response= render(request,'shift_templates/shift.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def shift_table_results(request):
    return  render(request,'shift_templates/shift_table_results.html',context=_show_shift(request))
       
# shift create form
@staff_member_required(login_url='/')
def shift_create(request):
    context={"warehouses":Warehouse.objects.all()}
    if request.method == "POST":
        form = CreateShiftForm(request.POST)
        if form.is_valid():
            shift=form.save(commit=False)  
            shift.create_user_pk = request.user.pk
            shift.create_user_username = request.user.username
            shift.save()
            form.save_m2m()
            create_product_shfit(shift)
            context['message']='Creado correctamente'
        else:
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'shift_templates/actions/shiftCreate/shiftCreateForm.html',context) 
    form = CreateShiftForm()
    context['form']=form
    return render(request,'shift_templates/actions/shiftCreate/shiftCreateForm.html',context) 


# shift update forms
@staff_member_required(login_url='/')
def shift_update(request,pk):
    shift = Shift.objects.filter(pk=pk).first()
    form = UpdateShiftForm(instance=shift)
    context={}
    context['shift']=shift
    context['form']=form
    return render(request,'shift_templates/actions/shiftUpdate/shiftUpdateForm.html',context) 

# shift main information update form
@staff_member_required(login_url='/')
def shift_form_update(request,pk):
    context={}
    if request.method == "POST":
        shift = Shift.objects.filter(pk=pk).first()
        form = UpdateShiftForm(request.POST,instance=shift)
        if form.is_valid():
            shift_form_valid=form.save(commit=False)
            form.save_m2m()
            shift_form_valid.save()
            message="Editado correctamente"
            context['message']=message
        else:
            message="Corrige los errores"
            context['error']=message
        context['shift']=shift
        context['form']=form
        return render(request,'shift_templates/actions/shiftUpdate/shiftUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def shift_delete(request,pk):
    shift = Shift.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if shift:
            shift_pk=shift.pk
            shift.delete()
            context = _show_shift(request)
            context['message']=f'{shift_pk} ha sido eliminada'
        else:
            context['error']=f'Lo sentimos, el turno no existe'
        return render(request,'shift_templates/shift_table_results.html',context)
    return  render(request,'shift_templates/actions/shiftDelete/shiftDeleteVerify.html',{"shift":shift})
     


# Show shift table
@staff_member_required(login_url='/')
def _show_shift(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    shifts = ShiftFilter(request.GET, queryset=Shift.objects.all().order_by('-id'))
    paginator = Paginator(shifts.qs, 200)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail shift table
@staff_member_required(login_url='/')
def shift_detail(request,pk):
    shift = Shift.objects.filter(pk=pk).first()
    
    return  render(request,'shift_templates/actions/shiftDetail/shiftDetail.html',{"shift":shift})
    
# Detail shift table
@staff_member_required(login_url='/')
def shift_report_detail(request,pk):
    shift = get_object_or_404(Shift,pk=pk)
    context={
        "shift":shift,
        "products":shift.product_shift_report.all().order_by('product__code'),
        "total_initial_cant":shift.total_initial_cant ,
        "total_products_sold":shift.total_sold_cant if shift.finish_date_at else shift.estimate_total_sold_cant,
        "total_warehouse_product_stock":shift.total_finish_cant if shift.finish_date_at else shift.estimate_finish_cant,
        "total_shift_product_import":shift.total_import if shift.finish_date_at else shift.estimate_total_import
    }
    return  render(request,'shift_templates/actions/shiftDetail/shiftReportDetail.html',context)
    
@group_required('administrador')
@staff_member_required(login_url='/')
def shift_close_report(request,pk):
    shift = get_object_or_404(Shift,pk=pk)
    closed_shift(shift)
    return redirect('shift_view')
     