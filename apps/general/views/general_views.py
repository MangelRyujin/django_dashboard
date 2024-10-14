from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login 
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from apps.general.models import SocialMedia, WhatsAppContact
from apps.products.models import Category,Product,Coupon
from utils.funtions.sales.sale import *
from utils.funtions.users.user import *
from ..decorators import user_is_not_authenticated
from apps.accounts.models import User
from django.contrib.admin.views.decorators import staff_member_required
from apps.general.forms.register_form import RegisterForm
from utils.funtions.products.product import *


# Dashboard view (index)
# @login_required(login_url='/login/')
@staff_member_required(login_url='/')
def dashboard_view(request):
    
    admin_history = User.history.filter(is_staff=True)[:10]
    user_history = User.history.filter(is_staff=False)[:10]
    coupon_history = Coupon.history.all()[:10]
    category_history = Category.history.all()[:10]
    product_history = Product.history.all()[:10]
    porcent_float,porcent_int = sales_goal()
    context={
        'dashboard_favorite_products':dashboard_favorite_products(),
        'total_users':total_users(),
        'total_orders':total_orders(),
        'porcent_float':porcent_float,
        'porcent_int':porcent_int,
        'total_sold_out_products':total_sold_out_products(),
        'total_new_orders':total_new_orders(),
        'total_products':total_products(),
        'total_sales':total_sales(),
        'total_reviews':total_reviews(),
        'total_products_views':total_products_views(),
        'total_positive_reviews':total_positive_reviews(),
        'total_available_products':total_available_products(),
        'admin_history':admin_history,
        'category_history':category_history,
        'product_history':product_history,
        'user_history':user_history,
        'coupon_history':coupon_history,
    }
    response= render(request,'index.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response



# Log in view
@user_is_not_authenticated
def login_view(request):
    
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url =  request.POST.get('next_url','')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponse()
            response["HX-Redirect"]= next_url if next_url else '/'
            return response
        else:
            return HttpResponse(f"""
                                 <div class="alert alert-dismissible alert-danger d-flex align-items-center mb-0 mt-4 px-2 fade show" role="alert">
                      
                        <div class="small px-1 me-2 text-danger-emphasis">
                          Credenciales incorrectas
                        </div>
                        <span type="button" class="btn-close px-2" data-bs-dismiss="alert" aria-label="Close"></span>
                      </div>
                                
                                """)
    context = {
        "whatsapp":WhatsAppContact.objects.first(),
        "social":SocialMedia.objects.first(),
        "next_url":request.GET.get('next', '')
    }
    return render(request, 'login.html',context)

# Register in view
@user_is_not_authenticated
def register_view(request):
    context = {
        "whatsapp":WhatsAppContact.objects.first(),
        "social":SocialMedia.objects.first(),
        "form":RegisterForm(request.POST or None)
    }
    return render(request, 'register.html',context)

# Register in view
@user_is_not_authenticated
def register_form_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            response = render(request, 'login.html')
            response["HX-Redirect"]= '/login/'
            return response
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'shop_templates/register/register_form.html',{"form":form})


# Change password view
@login_required(login_url='/login/')
def change_password_view(request):
    form = PasswordChangeForm(user=request.user)
    response= render(request, 'change_password/change_password.html',{"form":form})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Change password form component
@login_required(login_url='/login/')
def change_password_form(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse()
            response["HX-Redirect"]= '/login/'
            return response
        else:
            return render(request, 'change_password/change_password_form.html',{"form":form})
        
