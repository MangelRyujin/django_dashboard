from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group
from apps.accounts.models import User
from apps.accounts.filters import UserFilter
from apps.accounts.forms.admin_forms import  SingUpForm,ChangeAdminForm
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.core.paginator import Paginator
import logging
logger = logging.getLogger(__name__)

# user view (index)
@login_required(login_url='/login/')
def user_view(request):
    response= render(request,'user_templates/user.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@login_required(login_url='/login/')
def user_table_results(request):
    return  render(request,'user_templates/user_table_results.html',context=_show_user(request))
       
# admin create form
@login_required(login_url='/login/')
def admin_create(request):
    form = SingUpForm(request.POST or None)
    groups = Group.objects.all()
    context={
        'form':form,
        'groups':groups
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()  
            context['message']='Created successfully'
        else:
            context['error']='Correct the errors'
    return render(request,'admin_templates/actions/adminCreate/adminCreateForm.html',context) 


# admin update forms
@login_required(login_url='/login/')
def admin_update(request,pk):
    admin = User.objects.filter(pk=pk).first()
    form = ChangeAdminForm(instance=admin)
    pass_form = AdminPasswordChangeForm(user=admin)
    context={}
    context['admin']=admin
    context['form']=form
    context['pass_form']=pass_form
    return render(request,'admin_templates/actions/adminUpdate/adminUpdateForm.html',context) 

# admin main information update form
@login_required(login_url='/login/')
def admin_main_information_update(request,pk):
    context={}
    if request.method == "POST":
        admin = User.objects.filter(pk=pk).first()
        form = ChangeAdminForm(request.POST,request.FILES,instance=admin)
        if form.is_valid():
            admin_form_valid=form.save(commit=False)
            admin_form_valid._change_reason = f'Modifying personal information for the {admin.username} administrator'
            admin_form_valid.save()
            form.save_m2m()
            message="Change admin successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['admin']=admin
        context['form']=form
        return render(request,'admin_templates/actions/adminUpdate/mainAdminUpdate.html',context) 


# admin password update form
@login_required(login_url='/login/')
def admin_password_update(request,pk):
    context={}
    if request.method == "POST":
        admin = User.objects.filter(pk=pk).first()
        pass_form = AdminPasswordChangeForm(admin,request.POST)
        if pass_form.is_valid():
            admin_form_valid = pass_form.save(commit=False)
            admin_form_valid._change_reason = f"Modifying the password for the {admin.username} administrator"
            admin_form_valid.save()
            message="Change password successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['admin']=admin
        context['pass_form']=pass_form
        return render(request,'admin_templates/actions/adminUpdate/passAdminUpdate.html',context) 


# Delete result table
@login_required(login_url='/login/')
def admin_delete(request,pk):
    admin = User.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if admin:
            admin_name=admin.username
            admin.delete()
            context = _show_user(request)
            context['message']=f'{admin_name} has been delete'
        else:
            context['error']=f'Sorry, admin not found'
        return render(request,'admin_templates/admin_table_results.html',context)
    return  render(request,'admin_templates/actions/adminDelete/adminDeleteVerify.html',{"admin":admin})
     


# Show user table
def _show_user(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    users = UserFilter(request.GET, queryset=User.objects.exclude(groups__isnull=True).order_by('-id'))
    paginator = Paginator(users.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user table
@login_required(login_url='/login/')
def user_detail(request,pk):
    user = User.objects.filter(pk=pk).first()
    return  render(request,'user_templates/actions/userDetail/userDetail.html',{"user":user})
     