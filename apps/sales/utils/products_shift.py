from django.db.models import Sum
from apps.products.models import Product
from apps.sales.models import ProductShiftReport
from datetime import date, datetime


def create_product_shfit(shift):
    warehouses = shift.warehouse.all()
    
    for warehouse in warehouses:
        products=warehouse.warehouse_stock.values('product__pk','product__code','product__name').filter(is_active=True).annotate(
            count= Sum('cant'),
        ).order_by('product__code')
        for product in products:
            product_shift = ProductShiftReport.objects.filter(
                shift=shift,
                product__pk=product['product__pk']
            ).first()
            if product_shift:
                product_shift.initial_cant+= product['count']
                product_shift.save()
            else:
                ProductShiftReport.objects.create(
                    shift=shift,
                    product=Product.objects.get(pk=product['product__pk']),
                    initial_cant=product['count'],
                    total_price=0
                )


def closed_shift(shift):
    products=ProductShiftReport.objects.filter(shift=shift)
    for product in products:
        product.sold_cant= product.estimate_products_sold
        product.finish_cant= product.estimate_warehouse_product_stock
        product.total_price= product.estimate_shift_product_import
        product.shift.finish_date_at= date.today()
        product.shift.finish_time_at= datetime.now()
        product.save()
        product.shift.save()