from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Warehouse)
admin.site.register(CategoryStock)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(Facture)
admin.site.register(StockMovements)