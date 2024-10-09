from apps.sales.models import LocalOrder, Order

def total_sales():
    return sum(order.total_price for order in Order.objects.all()) or 0

def total_new_orders():
    return LocalOrder.objects.filter(state='p').__len__() or 0