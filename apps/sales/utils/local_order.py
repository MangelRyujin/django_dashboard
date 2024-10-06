from apps.sales.models import Order

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


# Payment methods proccess
def order_paid_method(order_unpaid,method,cash,transfer):
    if method == 'c':
            order_paid_cash(order_unpaid)
    if method == 't':
            order_paid_transfer(order_unpaid)
    if method == 'b':
            order_paid_both(order_unpaid,cash,transfer)
        