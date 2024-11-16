from django.shortcuts import render
from apps.accounts.decorators import group_required
from apps.products.filters import CategoryFilter
from apps.products.forms.category_forms import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
import logging
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required

# category view (index)
@group_required('administrador')
@staff_member_required(login_url='/')
def category_view(request):
    response= render(request,'category_templates/category.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def category_table_results(request):
    return  render(request,'category_templates/category_table_results.html',context=_show_category(request))
       
# category create form
@staff_member_required(login_url='/')
def category_create(request):
    context={}
    
    if request.method == "POST":
        form = UpdateCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()  
            context['message']='Creado correctamente'
        else:
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'category_templates/actions/categoryCreate/categoryCreateForm.html',context) 
    form = CreateCategoryForm()
    context['form']=form
    return render(request,'category_templates/actions/categoryCreate/categoryCreateForm.html',context) 


# category update forms
@staff_member_required(login_url='/')
def category_update(request,pk):
    category = Category.objects.filter(pk=pk).first()
    form = UpdateCategoryForm(instance=category)
    context={}
    context['category']=category
    context['form']=form
    return render(request,'category_templates/actions/categoryUpdate/categoryUpdateForm.html',context) 

# category main information update form
@staff_member_required(login_url='/')
def category_form_update(request,pk):
    context={}
    if request.method == "POST":
        category = Category.objects.filter(pk=pk).first()
        form = UpdateCategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            category_form_valid=form.save(commit=False)
            category_form_valid._change_reason = f'Categoría {category.name} modificada'
            category_form_valid.save()
            message="Editado correctamente"
            context['message']=message
        else:
            message="Corrige los errores"
            context['error']=message
        context['category']=category
        context['form']=form
        return render(request,'category_templates/actions/categoryUpdate/categoryUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def category_delete(request,pk):
    category = Category.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if category:
            category_name=category.name
            category.delete()
            context = _show_category(request)
            context['message']=f'{category_name} ha sido eliminada'
        else:
            context['error']=f'Lo sentimos, la categoría no existe'
        return render(request,'category_templates/category_table_results.html',context)
    return  render(request,'category_templates/actions/categoryDelete/categoryDeleteVerify.html',{"category":category})
     


# Show category table
@staff_member_required(login_url='/')
def _show_category(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    categorys = CategoryFilter(request.GET, queryset=Category.objects.all().order_by('-id'))
    paginator = Paginator(categorys.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user category table
@staff_member_required(login_url='/')
def category_detail(request,pk):
    category = Category.objects.filter(pk=pk).first()
    return  render(request,'category_templates/actions/categoryDetail/categoryDetail.html',{"category":category})
     