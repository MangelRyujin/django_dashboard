from django.urls import path
from apps.shop.views.product_detail import shop_product_detail_view
from apps.shop.views.products_store_views import *
from apps.shop.views.shop_views import *

urlpatterns = [
    path('',shop_view,name='shop_view'),
    path('products/',products_store_view,name='products_store_view'),
    path('product-detail/',shop_product_detail_view,name='shop_product_detail_view'),
    
]

