from apps.general.models import Goal
from apps.sales.models import LocalOrder, Order, ShopOrder

def total_orders():
    return Order.objects.all().count() or 0

def total_sales():
    return sum(order.total_price for order in Order.objects.all()) or 0

def total_new_orders():
    return LocalOrder.objects.filter(state='p').__len__() + ShopOrder.objects.filter(state='p').__len__() or 0

def sales_goal():
    goal=Goal.objects.first()
    goal_value= goal.goal or 100000
    sales = sum(order.total_items for order in Order.objects.all()) or 0
    return float(round((sales*100)/goal_value,2)),int(round((sales*100)/goal_value,2))