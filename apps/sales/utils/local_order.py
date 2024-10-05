

def items_discount_or_revert(order,action):
        local_order_items=order.localorderitem_set.all()
        if local_order_items.exists():
            for item in local_order_items:
                items_stock_discount_or_revert(item,action)
    
def items_stock_discount_or_revert(item,action):
        local_order_item_stocks=item.localorderitemstock_set.all()
        if local_order_item_stocks.exists():
            for stock in local_order_item_stocks:
                if action == "discount":
                    stock.stock.cant -= stock.cant
                else:
                    stock.stock.cant += stock.cant
                stock.stock.save()
                
                