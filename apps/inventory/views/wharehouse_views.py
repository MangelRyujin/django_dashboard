from django.shortcuts import render
from apps.inventory.filters import WharehouseFilter
from apps.inventory.forms.wharehouse_forms import CreateWharehouseForm, UpdateWharehouseForm
from apps.inventory.models import Wharehouse
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging
logger = logging.getLogger(__name__)

# category view (index)
@login_required(login_url='/login/')
def wharehouse_view(request):
    response= render(request,'wharehouse_templates/wharehouse.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@login_required(login_url='/login/')
def wharehouse_table_results(request):
    return  render(request,'wharehouse_templates/wharehouse_table_results.html',context=_show_wharehouse(request))
       
# category create form
@login_required(login_url='/login/')
def wharehouse_create(request):
    context={}
    if request.method == "POST":
        form = CreateWharehouseForm(request.POST)
        if form.is_valid():
            form.save()  
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
        context['form']=form
        return render(request,'wharehouse_templates/actions/wharehouseCreate/wharehouseCreateForm.html',context) 
    form = CreateWharehouseForm()
    context['form']=form
    return render(request,'wharehouse_templates/actions/wharehouseCreate/wharehouseCreateForm.html',context) 


# category update forms
@login_required(login_url='/login/')
def wharehouse_update(request,pk):
    wharehouse = Wharehouse.objects.filter(pk=pk).first()
    form = UpdateWharehouseForm(instance=wharehouse)
    context={}
    context['wharehouse']=wharehouse
    context['form']=form
    return render(request,'wharehouse_templates/actions/wharehouseUpdate/wharehouseUpdateForm.html',context) 

# wharehouse main information update form
@login_required(login_url='/login/')
def wharehouse_form_update(request,pk):
    context={}
    if request.method == "POST":
        wharehouse = Wharehouse.objects.filter(pk=pk).first()
        form = UpdateWharehouseForm(request.POST,request.FILES,instance=wharehouse)
        if form.is_valid():
            wharehouse_form_valid=form.save(commit=False)
            wharehouse_form_valid._change_reason = f'Modifying wharehouse {wharehouse.name}'
            wharehouse_form_valid.save()
            message="Change wharehouse successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['wharehouse']=wharehouse
        context['form']=form
        return render(request,'wharehouse_templates/actions/wharehouseUpdate/wharehouseUpdateCheckForm.html',context) 


# Delete result table
@login_required(login_url='/login/')
def wharehouse_delete(request,pk):
    wharehouse = Wharehouse.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if wharehouse:
            wharehouse_name=wharehouse.name
            wharehouse.delete()
            context = _show_wharehouse(request)
            context['message']=f'Wharehouse {wharehouse_name} has been delete'
        else:
            context['error']=f'Sorry, wharehouse not found'
        return render(request,'wharehouse_templates/wharehouse_table_results.html',context)
    return  render(request,'wharehouse_templates/actions/wharehouseDelete/wharehouseDeleteVerify.html',{"wharehouse":wharehouse})
     


# Show wharehouse table
def _show_wharehouse(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    wharehouses = WharehouseFilter(request.GET, queryset=Wharehouse.objects.all().order_by('-id'))
    paginator = Paginator(wharehouses.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context
