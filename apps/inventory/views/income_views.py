from django.shortcuts import render
from apps.inventory.filters import IncomeFilter
from apps.inventory.forms.income_forms import *
from django.core.paginator import Paginator
import logging
from django.contrib.admin.views.decorators import staff_member_required
logger = logging.getLogger(__name__)

# income view (index)
@staff_member_required(login_url='/')
def income_view(request):
    response= render(request,'income_templates/income.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def income_table_results(request):
    return  render(request,'income_templates/income_table_results.html',context=_show_income(request))
       
# income create form
@staff_member_required(login_url='/')
def income_create(request):
    context={}
    if request.method == "POST":
        form = CreateIncomeForm(request.POST)
        if form.is_valid():
            income=form.save(commit=False)
            income.created_user=request.user
            income.save()  
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
        context['form']=form
        return render(request,'income_templates/actions/incomeCreate/incomeCreateForm.html',context) 
    form = CreateIncomeForm()
    context['form']=form
    return render(request,'income_templates/actions/incomeCreate/incomeCreateForm.html',context) 


# income update forms
@staff_member_required(login_url='/')
def income_update(request,pk):
    income = Income.objects.filter(pk=pk).first()
    form = UpdateIncomeForm(instance=income)
    context={}
    context['income']=income
    context['form']=form
    return render(request,'income_templates/actions/incomeUpdate/incomeUpdateForm.html',context) 

# income main information update form
@staff_member_required(login_url='/')
def income_form_update(request,pk):
    context={}
    if request.method == "POST":
        income = Income.objects.filter(pk=pk).first()
        form = UpdateIncomeForm(request.POST,instance=income)
        if form.is_valid():
            form.save()
            message="Change income successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['income']=income
        context['form']=form
        return render(request,'income_templates/actions/incomeUpdate/incomeUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def income_delete(request,pk):
    income = Income.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if income:
            income_code=income.pk
            income.delete()
            context = _show_income(request)
            context['message']=f'Income {income_code} has been delete'
        else:
            context['error']=f'Sorry, income not found'
        return render(request,'income_templates/income_table_results.html',context)
    return  render(request,'income_templates/actions/incomeDelete/incomeDeleteVerify.html',{"income":income})
     


# Show income table
@staff_member_required(login_url='/')
def _show_income(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    incomes = IncomeFilter(request.GET, queryset=Income.objects.all().order_by('-id'))
    paginator = Paginator(incomes.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user income table
@staff_member_required(login_url='/')
def income_detail(request,pk):
    income = Income.objects.filter(pk=pk).first()
    return  render(request,'income_templates/actions/incomeDetail/incomeDetail.html',{"income":income})
     