from apps.products.models import Product,ProductReview


# Calculate total products sold cant
def products_sold():
    return sum(product.total_sales for product in Product.objects.all() if product.total_stock > 0) or 0



def total_products():
    return Product.objects.all().__len__()

def total_sold_out_products():
    count = 0
    for product in  Product.objects.all():
        if product.total_stock <= 0:
            count=count + 1
    return count

def total_available_products():
    count = 0
    for product in  Product.objects.all():
        if product.total_stock > 0:
            count=count + 1
    return count

def total_reviews():
    return ProductReview.objects.filter(stars__gt=3).__len__()