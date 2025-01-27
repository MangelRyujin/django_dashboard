from decimal import Decimal
from apps.sales.models import Order, OrderItem, OrderItemStock

# Discount all tiems stock for shop order
def shop_items_discount_or_revert(order,action):
        shop_order_items=order.shoporderitem_set.all()
        if shop_order_items.exists():
            for item in shop_order_items:
                shop_items_stock_discount_or_revert(item,action)

# Discount all tiems stock for shop order item
def shop_items_stock_discount_or_revert(item,action):
        shop_order_item_stocks=item.shoporderitemstock_set.all()
        if shop_order_item_stocks.exists():
            for stock in shop_order_item_stocks:
                if action == "discount":
                    stock.stock.cant -= stock.cant
                else:
                    stock.stock.cant += stock.cant
                stock.stock.save()
   

             
# Payment method cash     
def shop_order_paid_cash(order_unpaid,user):
    order = Order.objects.create(
          user_create = user,
          user_id= order_unpaid.created_user.pk,
          user_ci = order_unpaid.created_user.ci,
          user_full_name=  f'{order_unpaid.created_user.first_name} {order_unpaid.created_user.last_name}' if order_unpaid.created_user.first_name and order_unpaid.created_user.last_name else order_unpaid.created_user.username,
          user_phone =  order_unpaid.phone,
          address= order_unpaid.address,
          type = 's',
          payment_type= 'c',
          cash = order_unpaid.total_price,
          transfer= 0,
        )
    order.save()
    shop_order_paid_created_items(order,order_unpaid)
    
# Payment method transfer
def shop_order_paid_transfer(order_unpaid,user):
    order = Order.objects.create(
          user_create = user,
          user_id= order_unpaid.created_user.pk,
          user_ci = order_unpaid.created_user.ci,
          user_full_name=  f'{order_unpaid.created_user.first_name} {order_unpaid.created_user.last_name}' if order_unpaid.created_user.first_name and order_unpaid.created_user.last_name else order_unpaid.created_user.username,
          user_phone =  order_unpaid.phone,
          address= order_unpaid.address,
          type = 's',
          payment_type= 't',
          cash = 0,
          transfer= order_unpaid.total_price,
        )
    order.save()
    shop_order_paid_created_items(order,order_unpaid)

# Payment method both
def shop_order_paid_both(order_unpaid,cash,transfer,user):
    order = Order.objects.create(
          user_create = user,
          user_id= order_unpaid.created_user.pk,
          user_ci = order_unpaid.created_user.ci,
          user_full_name=  f'{order_unpaid.created_user.first_name} {order_unpaid.created_user.last_name}' if order_unpaid.created_user.first_name and order_unpaid.created_user.last_name else order_unpaid.created_user.username,
          user_phone =  order_unpaid.phone,
          address= order_unpaid.address,
          type = 's',
          payment_type= 'b',
          cash = cash,
          transfer= transfer,
        )
    order.save()
    shop_order_paid_created_items(order,order_unpaid)


# Payment methods proccess
def shop_order_paid_method(order_unpaid,method,cash,transfer,user):
    if method == 'c':
            shop_order_paid_cash(order_unpaid,user)
    if method == 't':
            shop_order_paid_transfer(order_unpaid,user)
    if method == 'b':
            shop_order_paid_both(order_unpaid,cash,transfer,user)

def shop_order_paid_created_items(order,order_unpaid):
    for item in order_unpaid.shoporderitem_set.all():
        order_item=OrderItem.objects.create(
            order=order,
            product_id = item.product.id,
            product_name = item.product.name,
            cant = item.cant,
            total_cost = item.total_cost,
            total_price = item.price
        )
        item.product.total_sales+=item.cant
        item.product.save()
        order_item.save()
        shop_order_paid_created_item_stocks(item,order_item)
        

def shop_order_paid_created_item_stocks(item,order_item):
    for stock in item.shoporderitemstock_set.all():
        order_item_stock = OrderItemStock.objects.create(
            item=order_item,
            stock_code = stock.stock.code,
            stock_name = stock.stock.name,
            stock_unit_price = stock.stock.unit_price,
            cant = stock.cant,
            stock_cant_affter = stock.stock.cant,
            stock_cant_before = stock.stock.cant + stock.cant,
            stock_wharehouse_id = stock.stock.warehouse.pk,
            stock_wharehouse_name = stock.stock.warehouse.name,
            product_import = stock.cant * (order_item.total_price/order_item.cant)
        )
        order_item_stock.save()


# Payment methods proccess data
def shop_order_paid_proccess_data(data,total_price):
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

