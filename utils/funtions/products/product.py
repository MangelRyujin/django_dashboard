from apps.products.models import Product,ProductReview


# Calculate total products sold cant
def products_sold():
    return sum(product.total_sales for product in Product.objects.all() if product.total_stock > 0) or 0

# Calculate total products
def total_products():
    return Product.objects.all().__len__()

# Calculate total products sold out
def total_sold_out_products():
    count = 0
    for product in  Product.objects.all():
        if product.total_stock <= 0:
            count=count + 1
    return count

# Calculate total available products
def total_available_products():
    count = 0
    for product in  Product.objects.all():
        if product.total_stock > 0:
            count=count + 1
    return count

# Calculate total positive reviews
def total_reviews():
    return ProductReview.objects.filter(stars__gt=3).__len__()

# Filter 12 cheap products
def cheap_products(user):
    cheap_products=[]
    products = Product.objects.filter(is_active=True).order_by("price")[:12]
    for product in products:
            like=product.user_has_like(user.id)
            cheap_products.append(
                {
                    'like':like,
                    'product':product
                }
            )
    return cheap_products

# Filter 6 favorite products
def favorite_products(user):
    favorite_products=[]
    products = Product.objects.filter(is_active=True).order_by("-total_sales")[:6]
    for product in products:
        like=product.user_has_like(user.id)
        favorite_products.append(
            {
                'like':like,
                'product':product
            }
        )
    return favorite_products