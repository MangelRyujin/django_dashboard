from django.shortcuts import render
from apps.accounts.decorators import group_required
from apps.products.filters import  CouponFilter
from apps.products.forms.category_forms import *
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator
from apps.accounts.models import User
import logging
from django.contrib.admin.views.decorators import staff_member_required
from apps.products.forms.coupon_forms import CreateCouponForm, UpdateCouponForm
from apps.products.models import Coupon, Product
logger = logging.getLogger(__name__)

# coupon view (index)
@group_required('administrador')
@staff_member_required(login_url='/')
def coupon_view(request):
    context = {
        'users':User.objects.filter(is_staff=False,is_active=True),
        'products':Product.objects.filter(is_active=True)
    }
    response= render(request,'coupon_templates/coupon.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def coupon_table_results(request):
    return  render(request,'coupon_templates/coupon_table_results.html',context=_show_coupon(request))
       
# coupon create form
@staff_member_required(login_url='/')
def coupon_create(request):
    context={}
    context['users']=User.objects.filter(is_active=True,is_staff=False)
    context['products']=Product.objects.filter(is_active=True)
    if request.method == "POST":
        form = CreateCouponForm(request.POST)
        if form.is_valid():
            form.save()  
            context['message']='Creado correctamente'
        else:
            context['error']='Corrige los errores'
        context['form']=form
        return render(request,'coupon_templates/actions/couponCreate/couponCreateForm.html',context) 
    form = CreateCouponForm()
    context['form']=form
    
    return render(request,'coupon_templates/actions/couponCreate/couponCreateForm.html',context) 


# coupon update forms
@staff_member_required(login_url='/')
def coupon_update(request,pk):
    coupon = Coupon.objects.filter(pk=pk).first()
    form = UpdateCouponForm(instance=coupon)
    context={}
    context['users']=User.objects.filter(is_active=True,is_staff=False)
    context['products']=Product.objects.filter(is_active=True)
    context['coupon']=coupon
    context['form']=form
    return render(request,'coupon_templates/actions/couponUpdate/couponUpdateForm.html',context) 

# coupon main information update form
@staff_member_required(login_url='/')
def coupon_form_update(request,pk):
    context={}
    context['users']=User.objects.filter(is_active=True,is_staff=False)
    context['products']=Product.objects.filter(is_active=True)
    if request.method == "POST":
        coupon = Coupon.objects.filter(pk=pk).first()
        form = UpdateCouponForm(request.POST,request.FILES,instance=coupon)
        if form.is_valid():
            coupon_form_valid=form.save(commit=False)
            coupon_form_valid._change_reason = f'Cupón {coupon.code} modificado'
            coupon_form_valid.save()
            message="Editado correctamente"
            context['message']=message
        else:
            message="Corrige los errores"
            context['error']=message
        context['coupon']=coupon
        context['form']=form
        return render(request,'coupon_templates/actions/couponUpdate/couponUpdateCheckForm.html',context) 


# Delete result table
@staff_member_required(login_url='/')
def coupon_delete(request,pk):
    coupon = Coupon.objects.filter(pk=pk).first()
    context={}
    if request.method == "POST":
        if coupon:
            coupon_code=coupon.code
            coupon.delete()
            context = _show_coupon(request)
            context['message']=f'{coupon_code} ha sido eliminado'
        else:
            context['error']=f'Lo sentimos, el cupón no existe'
        return render(request,'coupon_templates/coupon_table_results.html',context)
    return  render(request,'coupon_templates/actions/couponDelete/couponDeleteVerify.html',{"coupon":coupon})
     


# Show category table
@staff_member_required(login_url='/')
def _show_coupon(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    coupons = CouponFilter(request.GET, queryset=Coupon.objects.all())
    paginator = Paginator(coupons.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context
