from django.urls import path
from apps.shop.views.product_detail import shop_product_detail_view
from apps.shop.views.products_store_views import *
from apps.shop.views.shop_views import *

urlpatterns = [
    path('',shop_view,name='shop_view'),
    path('products/',products_store_view,name='products_store_view'),
    path('product-detail/',shop_product_detail_view,name='shop_product_detail_view'),
    path('product_like/<int:pk>/',product_like,name='product_like'),
    path('product_cheap_like/<int:pk>/',product_cheap_like,name='product_cheap_like'),
    path('search_product/',search_product,name='search_product'),
    path('product_list_results/',product_list_results,name='product_list_results'),
    
    
]

