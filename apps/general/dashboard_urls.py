from django.urls import path,include
from apps.general.views import dashboard_view, sales_view
from apps.products.views.category_views import *

urlpatterns = [
    path('',dashboard_view,name='dashboard_view'),
    path('admins/',include('apps.accounts.urls.admin_urls')),
    path('users/',include('apps.accounts.urls.user_urls')),
    path('categories/',include('apps.products.urls.category_urls')),
    path('products/',include('apps.products.urls.product_urls')),
    path('category_stocks/',include('apps.inventory.urls.category_stock_urls')),
    path('warehouses/',include('apps.inventory.urls.warehouse_urls')),
    path('factures/',include('apps.inventory.urls.facture_urls')),
    path('stocks/',include('apps.inventory.urls.stock_urls')),
    path('suppliers/',include('apps.inventory.urls.supplier_urls')),
    path('stocks_movements/',include('apps.inventory.urls.stock_movements_urls')),
    path('reviews/',include('apps.products.urls.product_review_urls')),
    path('coupons/',include('apps.products.urls.coupon_urls')),
    path('orders/',include('apps.sales.urls.order_urls')),
    path('orders_settings/',include('apps.sales.urls.order_settings_urls')),
    
    
    path('sales/',sales_view,name='sales_view'),
]

