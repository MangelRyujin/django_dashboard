from django.shortcuts import render
from apps.accounts.decorators import group_required
from apps.products.filters import OffertFilter
from apps.products.forms.offert_forms import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required

# offert view (index)
@group_required('administrador')
@staff_member_required(login_url='/')
def offert_view(request):
    response= render(request,'offert_templates/offert.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def offert_table_results(request):
    return  render(request,'offert_templates/offert_table_results.html',context=_show_offert(request))
       
# offert create form
@staff_member_required(login_url='/')
def offert_create(request):
    context={}
    
    if request.method == "POST":
        form = UpdateOffertForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
            context['message']='Creado correctamente'
        else:
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'offert_templates/actions/offertCreate/offertCreateForm.html',context) 
    form = CreateOffertForm()
    context['form']=form
    return render(request,'offert_templates/actions/offertCreate/offertCreateForm.html',context) 


# offert update forms
@staff_member_required(login_url='/')
def offert_update(request,pk):
    offert = Offert.objects.filter(pk=pk).first()
    form = UpdateOffertForm(instance=offert)
    context={}
    context['offert']=offert
    context['form']=form
    return render(request,'offert_templates/actions/offertUpdate/offertUpdateForm.html',context) 

# offert main information update form
@staff_member_required(login_url='/')
def offert_form_update(request,pk):
    context={}
    if request.method == "POST":
        offert = Offert.objects.filter(pk=pk).first()
        form = UpdateOffertForm(request.POST,request.FILES,instance=offert)
        if form.is_valid():
            form.save()
            message="Editada correctamente"
            context['message']=message
        else:
            message="Corrige los errores"
            context['error']=message
        context['offert']=offert
        context['form']=form
        return render(request,'offert_templates/actions/offertUpdate/offertUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def offert_delete(request,pk):
    offert = Offert.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if offert:
            offert_name=offert.name
            offert.delete()
            context = _show_offert(request)
            context['message']=f'{offert_name} ha sido eliminada'
        else:
            context['error']=f'Lo sentimos, la oferta no existe'
        return render(request,'offert_templates/offert_table_results.html',context)
    return  render(request,'offert_templates/actions/offertDelete/offertDeleteVerify.html',{"offert":offert})
     


# Show offert table
@staff_member_required(login_url='/')
def _show_offert(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    offerts = OffertFilter(request.GET, queryset=Offert.objects.all().order_by('-id'))
    paginator = Paginator(offerts.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user offert table
@staff_member_required(login_url='/')
def offert_detail(request,pk):
    offert = Offert.objects.filter(pk=pk).first()
    return  render(request,'offert_templates/actions/offertDetail/offertDetail.html',{"offert":offert})
     