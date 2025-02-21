from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemStock)

admin.site.register(ShopOrder)
admin.site.register(ShopOrderItem)


    
class AdminProductShiftReport(admin.TabularInline):
    model = ProductShiftReport
    extra = 0

@admin.register(Shift)
class AdminShift(admin.ModelAdmin):
    list_display = ['pk', 'create_date_at','create_user_username']
    list_filter = ('create_user_username',)
    inlines = [AdminProductShiftReport,]
    list_per_page = 100
    
    
    
class AdminLocalOrderItem(admin.TabularInline):
    model = LocalOrderItem
    extra = 0

@admin.register(LocalOrder)
class AdminLocalOrder(admin.ModelAdmin):
    list_display = ['pk', ]
    inlines = [AdminLocalOrderItem,]
    list_per_page = 100