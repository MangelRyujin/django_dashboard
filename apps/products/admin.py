from django.contrib import admin

from apps.products.models import Category,Product,Coupon

# Register your models here.


admin.site.register(Category)

admin.site.register(Coupon)

admin.site.register(Product)