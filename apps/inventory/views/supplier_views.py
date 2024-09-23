from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group
from apps.accounts.models import User
from apps.inventory.filters import SupplierFilter
from apps.inventory.forms.supplier_forms import CreateSupplierForm,UpdateSupplierForm
from django.core.paginator import Paginator
import logging
from django.contrib.admin.views.decorators import staff_member_required
from apps.inventory.models import Supplier
logger = logging.getLogger(__name__)

# supplier view (index)
@staff_member_required(login_url='/shop')
def supplier_view(request):
    response= render(request,'supplier_templates/supplier.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/shop')
def supplier_table_results(request):
    return  render(request,'supplier_templates/supplier_table_results.html',context=_show_supplier(request))
       
# supplier create form
@staff_member_required(login_url='/shop')
def supplier_create(request):
    form = CreateSupplierForm()
    context={}
    
    if request.method == "POST":
        form = CreateSupplierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
    context['form']=form   
    return render(request,'supplier_templates/actions/supplierCreate/supplierCreateForm.html',context) 


# supplier update forms
@staff_member_required(login_url='/shop')
def supplier_update(request,pk):
    supplier = Supplier.objects.filter(pk=pk).first()
    form = UpdateSupplierForm(instance=supplier)
    
    context={}
    context['supplier']=supplier
    context['form']=form
    return render(request,'supplier_templates/actions/supplierUpdate/supplierUpdateForm.html',context) 

# supplier main information update form
@staff_member_required(login_url='/shop')
def supplier_form_update(request,pk):
    context={}
    if request.method == "POST":
        supplier = Supplier.objects.filter(pk=pk).first()
        form = UpdateSupplierForm(request.POST,request.FILES,instance=supplier)
        if form.is_valid():
            form.save()
            message="Change supplier successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['supplier']=supplier
        context['form']=form
        return render(request,'supplier_templates/actions/supplierUpdate/mainsupplierUpdate.html',context) 


# Delete result table
@staff_member_required(login_url='/shop')
def supplier_delete(request,pk):
    supplier = Supplier.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if supplier:
            supplier_name=f'{supplier.first_name} {supplier.last_name}'
            supplier.delete()
            context = _show_supplier(request)
            context['message']=f'{supplier_name} has been delete'
        else:
            context['error']=f'Sorry, supplier not found'
        return render(request,'supplier_templates/supplier_table_results.html',context)
    return  render(request,'supplier_templates/actions/supplierDelete/supplierDeleteVerify.html',{"supplier":supplier})
     


# Show supplier table
def _show_supplier(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    suppliers = SupplierFilter(request.GET, queryset=Supplier.objects.all().order_by('-id'))
    paginator = Paginator(suppliers.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user supplier table
@staff_member_required(login_url='/shop')
def supplier_detail(request,pk):
    supplier = Supplier.objects.filter(pk=pk).first()
    return  render(request,'supplier_templates/actions/supplierDetail/supplierDetail.html',{"supplier":supplier})
