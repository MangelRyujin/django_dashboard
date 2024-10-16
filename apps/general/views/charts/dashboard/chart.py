import calendar
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from datetime import date
from django.utils import timezone
from apps.sales.models import LocalOrder, Order
from datetime import timedelta
from django.db.models import Count
# Create your views here.


@staff_member_required
def get_total_items_orders(request):
    today = timezone.now().date()
    start_date = today - timedelta(days=6)
    end_date = today + timedelta(days=1)
    orders = Order.objects.filter(
    created_date__range=(start_date, end_date)
    ).order_by('created_date')
    total_items=0
    labels = []
    dataset_data = [0,0,0,0,0,0,0]
    current_label = None
    index=None
    current_date = today - timedelta(days=6)
    while current_date < end_date:
        label = current_date.strftime('%d')
        labels.append(label)
        current_date += timedelta(days=1)    
    for order in orders:
        label = order.created_date.strftime('%d')
        if label != current_label:
            current_label = label
            
            index=labels.index(label)
        dataset_data[index] += order.total_items
        total_items+=order.total_items
          
    return JsonResponse({
        "total_orders":total_items,
        "start_month":calendar.month_name[start_date.month],
        "end_month":calendar.month_name[end_date.month],
        "title": f"Product",
        "data": {
            "labels": labels,
            "datasets": [{
              "data": dataset_data,
            }]
        },
    })

@staff_member_required
def get_total_price_orders(request):
    today = timezone.now().date()
    start_date = today - timedelta(days=6)
    end_date = today + timedelta(days=1)
    orders = Order.objects.filter(
    created_date__range=(start_date, end_date)
    ).order_by('created_date')
    total_price=sum(order.total_price  for order in orders)
    labels = []
    dataset_data = [0,0,0,0,0,0,0]
    current_label = None
    index=None
    current_date = today - timedelta(days=6)
    while current_date < end_date:
        label = current_date.strftime('%d')
        labels.append(label)
        current_date += timedelta(days=1)    
    for order in orders:
        label = order.created_date.strftime('%d')
        if label != current_label:
            current_label = label
            index=labels.index(label)
        dataset_data[index] += order.total_price
          
    return JsonResponse({
        "total_price_orders":total_price,
        "start_month":calendar.month_name[start_date.month],
        "end_month":calendar.month_name[end_date.month],
        "title": f"Amount",
        "data": {
            "labels": labels,
            "datasets": [{
              "data": dataset_data,
            }]
        },
    })
    
@staff_member_required
def get_total_items_orders_month(request,year=timezone.now().year):
    orders = Order.objects.filter(
    created_date__year=year
    ).order_by('created_date')
    total_items=sum(order.total_items  for order in orders)
    labels = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    dataset_data = [0,0,0,0,0,0,0,0,0,0,0,0]
    for order in orders:
        label=order.created_date.month
        dataset_data[label-1] += order.total_items
    return JsonResponse({
        "total_items":total_items,
        "title": f"Products",
        "data": {
            "labels": labels,
            "datasets": [{
              "data": dataset_data,
            }]
        },
    })
    
@staff_member_required
def get_total_items_orders_price_month(request,year=timezone.now().year):
    orders = Order.objects.filter(
    created_date__year=year
    ).order_by('created_date')
    total_price=sum(order.total_price  for order in orders)
    labels = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    dataset_data = [0,0,0,0,0,0,0,0,0,0,0,0]
    for order in orders:
        label=order.created_date.month
        dataset_data[label-1] += order.total_price
    return JsonResponse({
        "total_price":total_price,
        "title": f"Amount",
        "data": {
            "labels": labels,
            "datasets": [{
              "data": dataset_data,
            }]
        },
    })