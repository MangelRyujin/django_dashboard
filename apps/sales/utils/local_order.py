from decimal import Decimal
from apps.sales.models import Order, OrderItem

# Discount all tiems stock for local order
def items_discount_or_revert(order,action):
        local_order_items=order.localorderitem_set.all()
        if local_order_items.exists():
            for item in local_order_items:
                items_stock_discount_or_revert(item,action)

# Discount all tiems stock for local order item
def items_stock_discount_or_revert(item,action):
        local_order_item_stocks=item.localorderitemstock_set.all()
        if local_order_item_stocks.exists():
            for stock in local_order_item_stocks:
                if action == "discount":
                    stock.stock.cant -= stock.cant
                else:
                    stock.stock.cant += stock.cant
                stock.stock.save()
   

             
# Payment method cash     
def order_paid_cash(order_unpaid):
    order = Order.objects.create(
          user_create = order_unpaid.user_create,
          user_ci = order_unpaid.user_ci,
          user_full_name= f'{order_unpaid.user_first_name} {order_unpaid.user_last_name}',
          user_phone =  order_unpaid.user_phone,
          address= order_unpaid.address,
          type = 'l',
          payment_type= 'c',
          cash = order_unpaid.total_price,
          transfer= 0,
        )
    order.save()
    
# Payment method transfer
def order_paid_transfer(order_unpaid):
    order = Order.objects.create(
          user_create = order_unpaid.user_create,
          user_ci = order_unpaid.user_ci,
          user_full_name= f'{order_unpaid.user_first_name} {order_unpaid.user_last_name}',
          user_phone =  order_unpaid.user_phone,
          address= order_unpaid.address,
          type = 'l',
          payment_type= 't',
          cash = 0,
          transfer= order_unpaid.total_price,
        )
    order.save()

# Payment method both
def order_paid_both(order_unpaid,cash,transfer):
    order = Order.objects.create(
          user_create = order_unpaid.user_create,
          user_ci = order_unpaid.user_ci,
          user_full_name= f'{order_unpaid.user_first_name} {order_unpaid.user_last_name}',
          user_phone =  order_unpaid.user_phone,
          address= order_unpaid.address,
          type = 'l',
          payment_type= 'b',
          cash = cash,
          transfer= transfer,
        )
    order.save()
    order_paid_created_items(order,order_unpaid)


# Payment methods proccess
def order_paid_method(order_unpaid,method,cash,transfer):
    if method == 'c':
            order_paid_cash(order_unpaid)
    if method == 't':
            order_paid_transfer(order_unpaid)
    if method == 'b':
            order_paid_both(order_unpaid,cash,transfer)

def order_paid_created_items(order,order_unpaid):
    for item in order_unpaid.localorderitem_set.all():
        order_item=OrderItem.objects.create(
            order=order,
            product_id = item.product.id,
            product_name = item.product.name,
            cant = item.cant,
            total_cost = item.total_cost,
            total_price = item.total_price
        )
        order_item.save()
     


# Payment methods proccess data
def order_paid_proccess_data(data,total_price):
    cash= Decimal(data["cash"] or 0 ) 
    transfer=Decimal(data["transfer"] or 0) 
    payment_type = data["payment_method"]
    if payment_type == 'c':
      data={
        "cash":total_price,
        "transfer":0,
        "total_paid" : total_price,
        "payment_type":payment_type,
        "total_price" : total_price 
        }
    elif payment_type == 't':
      data={
        "cash":0,
        "transfer":total_price,
        "total_paid" : total_price,
        "payment_type":payment_type,
        "total_price" : total_price
        }
    else:
        data={
            "cash":cash,
            "transfer":transfer,
            "total_paid" : total_price,
            "payment_type":payment_type,
            "total_price" : cash + transfer
            }
    return data

