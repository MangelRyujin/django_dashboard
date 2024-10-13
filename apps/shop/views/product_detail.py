from django.shortcuts import render
from apps.general.models import *

def shop_product_detail_view(request):
    context = {
        "whatsapp":WhatsAppContact.objects.first(),
        "social":SocialMedia.objects.first(),
    }
    response= render(request,'shop_templates/productDetail/product_detail.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
