from apps.products.models import Category, Offert, Product,ProductReview
from datetime import date
from django.db.models import Q

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

# Filter all categories
def categories_list_slider():
    categories = []
    category_query = Category.objects.filter(is_active=True)
    total_categories = category_query.count()
    
    full_groups = total_categories // 4

    for i in range(full_groups):
        group = list(category_query[i*4:(i+1)*4])
        categories.append(group)

    remaining = total_categories % 4
    if remaining > 0:
        categories.append(list(category_query[full_groups*4:]))

    return categories

# Filter offerts in date range
def offerts_actives():
    offerts= Offert.objects.filter(is_active=True).exclude(init_date__gt=date.today()).exclude(end_date__lt=date.today())
    return offerts

# Search all products
def search_all_products(request):
    if request.method == 'POST':
        keyword = request.POST.get("keyword",'')
        request.session['keyword'] = keyword
    search_products = Product.objects.filter(
        Q(name__icontains=keyword) | Q(categories__name__icontains=keyword)
        | Q(small_description__icontains=keyword)
        ).distinct().order_by('-id')[:20]
    context={
        'keyword':keyword,
        'products':search_products,
    }
    return context