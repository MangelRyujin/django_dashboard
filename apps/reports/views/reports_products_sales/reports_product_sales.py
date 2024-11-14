from django.shortcuts import render
import logging
from apps.inventory.models import Facture, Income, Spent
from apps.reports.filters import ReportFactureFilter, ReportIncomeFilter, ReportOrderItemFilter,ReportOrderFilter, ReportSpentFilter
from apps.sales.models import  Order, OrderItem
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
        count= Count('pk'),
        price=Sum('total_price'),
        cost=Sum('total_cost'),
        revenue=Sum('total_price')-Sum('total_cost')
        
    ).order_by('product_id')
    total_count=round(sum(item['count'] for item in items_grouped),2) 
    total_price=round(sum(item['price'] for item in items_grouped),2) 
    total_cost=round(sum(item['cost'] for item in items_grouped),2) 
    total_revenue=round(sum(item['revenue'] for item in items_grouped),2) 
    orders = ReportOrderFilter(request.GET, queryset=Order.objects.all())
    factures = ReportFactureFilter(request.GET, queryset=Facture.objects.all())
    incomes = ReportIncomeFilter(request.GET, queryset=Income.objects.all())
    spents = ReportSpentFilter(request.GET, queryset=Spent.objects.all())
    total_transfer = orders.qs.aggregate(total_transfer = Sum("transfer"))["total_transfer"] or 0
    total_cash = orders.qs.aggregate(total_cash=Sum("cash"))["total_cash"] or 0
    total_factures = sum(facture.total_amount for facture in factures.qs) or 0
    total_incomes = incomes.qs.aggregate(total=Sum("amount"))["total"] or 0
    total_spents = spents.qs.aggregate(total = Sum("amount"))["total"] or 0

    context={
        'total_count':total_count,
        'total_price':total_price,
        'total_cost':total_cost,
        'total_revenue':total_revenue,
        'items':items_grouped,
        'total_transfer':total_transfer,
        'total_cash':total_cash,
        'total_factures':total_factures,
        'total_incomes':total_incomes,
        'total_spents':total_spents,
        'total_spents_facture':total_spents+total_factures,
        'total_income_spents_facture':total_incomes-(total_spents+total_factures),
        'total_revenue_income_spents_facture':(total_revenue+total_incomes)-(total_spents+total_factures),

    }
    return context