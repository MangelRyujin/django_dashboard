from django.contrib import admin

from apps.products.models import Category, Offert, PrincipalCategory,Product,Coupon, ProductReview

# Register your models here.

admin.site.register(Offert)
admin.site.register(Category)
admin.site.register(PrincipalCategory)
admin.site.register(Coupon)

admin.site.register(Product)

admin.site.register(ProductReview)