from django.shortcuts import render
from apps.inventory.filters import SpentFilter
from apps.inventory.forms.spent_forms import *
from django.core.paginator import Paginator
import logging
from django.contrib.admin.views.decorators import staff_member_required
logger = logging.getLogger(__name__)

# spent view (index)
@staff_member_required(login_url='/')
def spent_view(request):
    response= render(request,'spent_templates/spent.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def spent_table_results(request):
    return  render(request,'spent_templates/spent_table_results.html',context=_show_spent(request))
       
# spent create form
@staff_member_required(login_url='/')
def spent_create(request):
    context={}
    if request.method == "POST":
        form = CreateSpentForm(request.POST)
        if form.is_valid():
            spent=form.save(commit=False)
            spent.created_user=request.user
            spent.save()  
            context['message']='Creado correctamente'
        else:
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'spent_templates/actions/spentCreate/spentCreateForm.html',context) 
    form = CreateSpentForm()
    context['form']=form
    return render(request,'spent_templates/actions/spentCreate/spentCreateForm.html',context) 


# spent update forms
@staff_member_required(login_url='/')
def spent_update(request,pk):
    spent = Spent.objects.filter(pk=pk).first()
    form = UpdateSpentForm(instance=spent)
    context={}
    context['spent']=spent
    context['form']=form
    return render(request,'spent_templates/actions/spentUpdate/spentUpdateForm.html',context) 

# spent main information update form
@staff_member_required(login_url='/')
def spent_form_update(request,pk):
    context={}
    if request.method == "POST":
        spent = Spent.objects.filter(pk=pk).first()
        form = UpdateSpentForm(request.POST,instance=spent)
        if form.is_valid():
            form.save()
            message="Editado correctamente"
            context['message']=message
        else:
            message="Corrige los errores"
            context['error']=message
        context['spent']=spent
        context['form']=form
        return render(request,'spent_templates/actions/spentUpdate/spentUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def spent_delete(request,pk):
    spent = Spent.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if spent:
            spent_code=spent.pk
            spent.delete()
            context = _show_spent(request)
            context['message']=f'Gasto {spent_code} ha sido eliminado'
        else:
            context['error']=f'Lo sentimos, el gasto no existe'
        return render(request,'spent_templates/spent_table_results.html',context)
    return  render(request,'spent_templates/actions/spentDelete/spentDeleteVerify.html',{"spent":spent})
     


# Show spent table
@staff_member_required(login_url='/')
def _show_spent(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    spents = SpentFilter(request.GET, queryset=Spent.objects.all().order_by('-id'))
    paginator = Paginator(spents.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user spent table
@staff_member_required(login_url='/')
def spent_detail(request,pk):
    spent = Spent.objects.filter(pk=pk).first()
    return  render(request,'spent_templates/actions/spentDetail/spentDetail.html',{"spent":spent})
     