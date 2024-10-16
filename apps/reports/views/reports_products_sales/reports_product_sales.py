from django.shortcuts import render
import logging
from apps.reports.filters import ReportOrderItemFilter
from apps.sales.models import  OrderItem
logger = logging.getLogger(__name__)
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Sum

# category view (index)
@staff_member_required(login_url='/')
def reports_sales_view(request):
    response = render(request,'reports_templates/reports_sales/reports_sales_template.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def reports_sales_view_results(request): 
    return  render(request,'reports_templates/reports_sales/reports_sales_results.html',context=_show_order(request))


# Show order table
@staff_member_required(login_url='/')
def _show_order(request):
    items_qs = ReportOrderItemFilter(request.GET, queryset=OrderItem.objects.all().order_by("product_id"))
    items_grouped = items_qs.qs.values('product_id','product_name').annotate(
        count=Count('pk'),
        price=Sum('total_price'),
        cost=Sum('total_cost'),
        revenue=Sum('total_price')-Sum('total_cost')
        
    ).order_by('product_id')
    total_count=sum(item['count'] for item in items_grouped)
    total_price=sum(item['price'] for item in items_grouped)
    total_cost=sum(item['cost'] for item in items_grouped)
    total_revenue=sum(item['revenue'] for item in items_grouped)
    context={
        'total_count':total_count,
        'total_price':total_price,
        'total_cost':total_cost,
        'total_revenue':total_revenue,
        'items':items_grouped,
    }
    return context