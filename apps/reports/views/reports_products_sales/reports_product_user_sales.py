from django.shortcuts import render
import logging
from apps.accounts.decorators import group_required
from apps.accounts.models import User
from apps.reports.filters import ReportUserOrderFilter, ReportUsersOrderItemFilter
from apps.sales.models import  Order, OrderItem
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum

# category view (index)
@group_required('administrador')
@staff_member_required(login_url='/')
def reports_user_sales_view(request):
    context={
        "users":User.objects.filter(is_staff=True).order_by("username")
    }
    response = render(request,'reports_templates/reports_user_sales/reports_sales_template.html',context)
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def reports_user_sales_view_results(request): 
    return  render(request,'reports_templates/reports_user_sales/reports_sales_results.html',context=_show_order(request))


# Show order table
@staff_member_required(login_url='/')
def _show_order(request):    
    if request.GET.get('user'):
        items_qs = ReportUsersOrderItemFilter(request.GET, queryset=OrderItem.objects.all().order_by("product_id"))
        items_grouped = items_qs.qs.values('product_id','product_name').annotate(
            count= Sum('cant'),
            price=Sum('total_price'),
        ).order_by('product_id')
    else:
        items_grouped = []
    total_count=round(sum(item['count'] for item in items_grouped),2) or 0
    total_price=round(sum(item['price'] for item in items_grouped),2) or 0
    orders = ReportUserOrderFilter(request.GET, queryset=Order.objects.all())
    total_transfer = orders.qs.aggregate(total_transfer = Sum("transfer"))["total_transfer"] or 0
    total_cash = orders.qs.aggregate(total_cash=Sum("cash"))["total_cash"] or 0

    context={
        'total_count':total_count,
        'total_price':total_price,
        'items':items_grouped,
        'total_transfer':total_transfer,
        'total_cash':total_cash,

    }
    return context