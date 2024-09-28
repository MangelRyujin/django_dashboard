from django.shortcuts import render
import logging
from apps.general.forms.general_forms import *
from apps.general.models import *
from django.contrib.admin.views.decorators import staff_member_required
logger = logging.getLogger(__name__)

# order view (index)
@staff_member_required(login_url='/shop')
def settings_view(request):
    header=PrincipalHeader.objects.first()
    local=LocalSales.objects.first()
    shop=ShopSales.objects.first()
    social=SocialMedia.objects.first()
    wapp=WhatsAppContact.objects.first()
    context={
        'header':header,
        'local':local,
        'shop':shop,
        'social':social,
        'wapp':wapp,
        'header_form': UpdatePrincipalHeaderForm(),
        'local_form': UpdateLocalSalesForm(),
        'shop_form': UpdateShopSalesForm(),
        'social_form': UpdateSocialMediaForm(),
        'wapp_form': UpdateWhatsAppContactForm(),
    }
    response= render(request,'settings_templates/settings.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


@staff_member_required(login_url='/shop')
def save_header_settings_view(request):
    context={}
    header=PrincipalHeader.objects.first()
    if request.method == "POST":
        if header:
            header_form=UpdatePrincipalHeaderForm(request.POST,request.FILES,instance=header)
        else: 
            header_form=UpdatePrincipalHeaderForm(request.POST,request.FILES)
        
        if header_form.is_valid():
            header_form.save()
            context['message']='Change successfully'
            context['header_form']=header_form
            
        else:
            context['error']='Correct the errors'
            context['header_form']=header_form
    context['header']=header
    return render(request,'settings_templates/forms/header_form.html',context) 
    

@staff_member_required(login_url='/shop')
def save_local_settings_view(request):
    context={}
    local = LocalSales.objects.first()
    if local:
        if local.is_active:
            print(local.is_active)
            local.is_active = False
            
        else:
            local.is_active = True
            
    local.save()
    context['local_change']=local
    return render(request,'settings_templates/forms/local_form.html',context) 
    
    

@staff_member_required(login_url='/shop')
def save_shop_settings_view(request):
    context={}
    shop=ShopSales.objects.first()
    
    if shop.is_active:
        shop.is_active = False
        
    else:
        shop.is_active = True
        
    shop.save()
    context['shop_change']=shop
    return render(request,'settings_templates/forms/shop_form.html',context) 
    
    
@staff_member_required(login_url='/shop')
def save_social_settings_view(request):
    context={}
    social=SocialMedia.objects.first()
    if request.method == "POST":
        if social:
            social_form=UpdateSocialMediaForm(request.POST,request.FILES,instance=social)
        else: 
            social_form=UpdateSocialMediaForm(request.POST,request.FILES)
        if social_form.is_valid():
            social_form.save()
            context['message']='Change successfully'
            context['social_form']=social_form
       
        else:
            context['error']='Correct the errors'
            context['social_form']=social_form
    context['social']=social
    return render(request,'settings_templates/forms/social_form.html',context) 
   
    
    

@staff_member_required(login_url='/shop')
def save_wapp_settings_view(request):
    context={}
    if request.method == "POST":
        wapp_form= UpdateWhatsAppContactForm(request.POST)
        if wapp_form.is_valid():
            wapp_form.save()
            context['message']='Change successfully'
            context['wapp_form']=wapp_form
        else:
            context['error']='Correct the errors'
            context['wapp_form']=wapp_form
    context['wapp']=WhatsAppContact.objects.first()
    return render(request,'settings_templates/forms/wapp_form.html',context) 
    