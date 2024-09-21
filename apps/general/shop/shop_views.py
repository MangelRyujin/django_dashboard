from django.shortcuts import render
from apps.general.models import *

def shop_view(request):
    return render(request,'shop.html')