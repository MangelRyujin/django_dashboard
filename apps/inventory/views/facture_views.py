from django.shortcuts import render
from apps.inventory.filters import FactureFilter
from apps.inventory.forms.facture_forms import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging

from apps.inventory.models import Supplier
from apps.products.models import Product
logger = logging.getLogger(__name__)

# facture view (index)
@login_required(login_url='/login/')
def facture_view(request):
    suppliers = Supplier.objects.all()
    response= render(request,'facture_templates/facture.html',{'suppliers':suppliers})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@login_required(login_url='/login/')
def facture_table_results(request):
    return  render(request,'facture_templates/facture_table_results.html',context=_show_facture(request))
       
# facture create form
@login_required(login_url='/login/')
def facture_create(request):
    context={
        'suppliers':Supplier.objects.all(),
        'products':Product.objects.all()
    }
    
    if request.method == "POST":
        form = CreateFactureForm(request.POST)
        if form.is_valid():
            form.save()  
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
        context['form']=form
        return render(request,'facture_templates/actions/factureCreate/factureCreateForm.html',context) 
    form = CreateFactureForm()
    context['form']=form
    return render(request,'facture_templates/actions/factureCreate/factureCreateForm.html',context) 


# facture update forms
@login_required(login_url='/login/')
def facture_update(request,pk):
    facture = Facture.objects.filter(pk=pk).first()
    form = UpdateFactureForm(instance=facture)
    context={}
    context['facture']=facture
    context['form']=form
    return render(request,'facture_templates/actions/factureUpdate/factureUpdateForm.html',context) 

# facture main information update form
@login_required(login_url='/login/')
def facture_form_update(request,pk):
    context={}
    if request.method == "POST":
        facture = Facture.objects.filter(pk=pk).first()
        form = UpdateFactureForm(request.POST,instance=facture)
        if form.is_valid():
            form.save()
            message="Change facture successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['facture']=facture
        context['form']=form
        return render(request,'facture_templates/actions/factureUpdate/factureUpdateCheckForm.html',context) 


# Delete result table
@login_required(login_url='/login/')
def facture_delete(request,pk):
    facture = Facture.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if facture:
            facture_code=facture.code
            facture.delete()
            context = _show_facture(request)
            context['message']=f'Facture {facture_code} has been delete'
        else:
            context['error']=f'Sorry, facture not found'
        return render(request,'facture_templates/facture_table_results.html',context)
    return  render(request,'facture_templates/actions/factureDelete/factureDeleteVerify.html',{"facture":facture})
     


# Show facture table
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
@login_required(login_url='/login/')
def facture_detail(request,pk):
    facture = Facture.objects.filter(pk=pk).first()
    return  render(request,'facture_templates/actions/factureDetail/factureDetail.html',{"facture":facture})
     