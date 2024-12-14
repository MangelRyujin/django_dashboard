from django.shortcuts import render
from apps.accounts.decorators import group_required
from apps.inventory.filters import FactureFilter
from apps.inventory.forms.facture_forms import *
from django.core.paginator import Paginator
import logging
from django.contrib.admin.views.decorators import staff_member_required
from apps.inventory.models import Supplier
from apps.products.models import Product
from utils.funtions.parce.parce_text_to_float import replace_parce_float
logger = logging.getLogger(__name__)

# facture view (index)
@group_required('administrador')
@staff_member_required(login_url='/')
def facture_view(request):
    suppliers = Supplier.objects.all()
    response= render(request,'facture_templates/facture.html',{'suppliers':suppliers})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def facture_table_results(request):
    return  render(request,'facture_templates/facture_table_results.html',context=_show_facture(request))
       
# facture create form
@staff_member_required(login_url='/')
def facture_create(request):
    context={
        'suppliers':Supplier.objects.all(),
        'products':Product.objects.all()
    }
    
    if request.method == "POST":
        form = CreateFactureForm(request.POST)
        if form.is_valid():
            form.save()  
            context['message']='Creada correctamente'
        else:
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'facture_templates/actions/factureCreate/factureCreateForm.html',context) 
    form = CreateFactureForm()
    context['form']=form
    return render(request,'facture_templates/actions/factureCreate/factureCreateForm.html',context) 


# facture update forms
@staff_member_required(login_url='/')
def facture_update(request,pk):
    facture = Facture.objects.filter(pk=pk).first()
    form = UpdateFactureForm(instance=facture)
    context={}
    context['facture']=facture
    context['form']=form
    return render(request,'facture_templates/actions/factureUpdate/factureUpdateForm.html',context) 

# facture main information update form
@staff_member_required(login_url='/')
def facture_form_update(request,pk):
    context={}
    if request.method == "POST":
        facture = Facture.objects.filter(pk=pk).first()
        data=request.POST.copy()
        data['unit_price'] = replace_parce_float(data['unit_price'])
        form = UpdateFactureForm(data,instance=facture)
        if form.is_valid():
            form.save()
            message="Editada correctamente"
            context['message']=message
        else:
            message="Corrige los errores"
            context['error']=message
        context['facture']=facture
        context['form']=form
        return render(request,'facture_templates/actions/factureUpdate/factureUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def facture_delete(request,pk):
    facture = Facture.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if facture:
            facture_code=facture.code
            facture.delete()
            context = _show_facture(request)
            context['message']=f'Factura {facture_code} ha sido eliminada'
        else:
            context['error']=f'Lo sentimos, la factura no existe'
        return render(request,'facture_templates/facture_table_results.html',context)
    return  render(request,'facture_templates/actions/factureDelete/factureDeleteVerify.html',{"facture":facture})
     


# Show facture table
@staff_member_required(login_url='/')
def _show_facture(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    factures = FactureFilter(request.GET, queryset=Facture.objects.all().order_by('-id'))
    paginator = Paginator(factures.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user facture table
@staff_member_required(login_url='/')
def facture_detail(request,pk):
    facture = Facture.objects.filter(pk=pk).first()
    return  render(request,'facture_templates/actions/factureDetail/factureDetail.html',{"facture":facture})
     