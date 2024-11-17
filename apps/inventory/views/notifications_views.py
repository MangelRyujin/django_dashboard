from apps.inventory.models import Stock
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q


def notifications():
    stocks= Stock.objects.all().order_by("cant")
    stock_in_danger=[stock for stock in stocks if stock.cant <= stock.storage_threshold]
    context={
        "stock_in_danger":stock_in_danger
    }
    return context

@staff_member_required(login_url='/')
def notification_view(request):
    return render(request,'notifications_templates/notifications.html',context=notifications())

@staff_member_required(login_url='/')
def notification_empty_view(request):
    return render(request,'notifications_templates/notifications_icon.html',context=notifications())

@staff_member_required(login_url='/')
def notification_results_view(request):
    return render(request,'notifications_templates/notifications_results.html',context=_show_notification(request))

# Show notification table
@staff_member_required(login_url='/')
def _show_notification(request):
    keyword = request.session.get('keyword', '')
    
    if request.method == 'POST':
        keyword = request.POST.get("keyword",'')
        request.session['keyword'] = keyword
        
    stocks = Stock.objects.filter(
         Q(name__icontains=keyword)
        | Q(warehouse__name__icontains=keyword)| Q(address__icontains=keyword)
        | Q(address__icontains=keyword)| Q(product__name__icontains=keyword)
        | Q(code__icontains=keyword) 
        ).distinct().order_by('cant')
    stock_in_danger=[stock for stock in stocks if stock.cant <= stock.storage_threshold]
    context={
        'stock_in_danger':stock_in_danger,
    }
    return context
