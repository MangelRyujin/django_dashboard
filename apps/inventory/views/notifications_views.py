from apps.inventory.models import Stock
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


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
