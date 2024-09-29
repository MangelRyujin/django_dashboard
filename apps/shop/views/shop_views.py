from django.shortcuts import render
from apps.general.models import *

def shop_view(request):
    response= render(request,'shop_templates/shop.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response