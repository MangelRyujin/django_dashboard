from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import Group
from apps.accounts.models import User
from apps.accounts.filters import UserFilter
from apps.accounts.forms.admin_forms import  SingUpForm,ChangeAdminForm
from django.contrib.auth.forms import AdminPasswordChangeForm,SetPasswordForm
from django.core.paginator import Paginator
import logging
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required

# user view (index)
@staff_member_required(login_url='/shop')
def user_view(request):
    response= render(request,'user_templates/user.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/shop')
def user_table_results(request):
    return  render(request,'user_templates/user_table_results.html',context=_show_user(request))
       
# admin create form
@staff_member_required(login_url='/shop')
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
@staff_member_required(login_url='/shop')
def user_update(request,pk):
    user = User.objects.filter(pk=pk).first()
    pass_form = SetPasswordForm(user=user)
    context={}
    context['user']=user
    context['pass_form']=pass_form
    return render(request,'user_templates/actions/userUpdate/userUpdateForm.html',context) 



# user password update form
@staff_member_required(login_url='/shop')
def user_password_update(request,pk):
    context={}
    if request.method == "POST":
        user = User.objects.filter(pk=pk).first()
        print(request.POST)
        
        pass_form = SetPasswordForm(user,request.POST)
        print(pass_form)
        if pass_form.is_valid():
            user_form_valid = pass_form.save(commit=False)
            user_form_valid._change_reason = f"Modifying the password for the user {user.username} "
            user_form_valid.save()
            message="Change password successfully"
            context['message']=message
        else:
            message="Correct the errors"
            context['error']=message
        context['user']=user
        context['pass_form']=pass_form
        return render(request,'user_templates/actions/userUpdate/passUserUpdate.html',context) 


# Delete result table
@staff_member_required(login_url='/shop')
def user_delete(request,pk):
    user = User.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if user:
            user_name=user.username
            context = _show_user(request)
            if user.is_active:
                user.is_active=False
                user._change_reason = f"User {user.username} has been ban"
                user.save()
                context['message']=f'{user_name} has been ban'
            else:
                user.is_active=True
                user._change_reason = f"User {user.username} has been active"
                user.save()
                context['message']=f'{user_name} has been active'
            
            
        else:
            context['error']=f'Sorry, user not found'
        return render(request,'user_templates/user_table_results.html',context)
    return  render(request,'user_templates/actions/userDelete/userDeleteVerify.html',{"user":user})
     


# Show user table
def _show_user(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    users = UserFilter(request.GET, queryset=User.objects.exclude(is_staff=True).order_by('-id'))
    paginator = Paginator(users.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user table
@staff_member_required(login_url='/shop')
def user_detail(request,pk):
    user = User.objects.filter(pk=pk).first()
    return  render(request,'user_templates/actions/userDetail/userDetail.html',{"user":user})
     