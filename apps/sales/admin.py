from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(LocalOrder)
admin.site.register(LocalOrderItem)
admin.site.register(ShopOrder)
admin.site.register(ShopOrderItem)