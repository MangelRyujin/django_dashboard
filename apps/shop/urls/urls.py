from django.urls import path
from apps.shop.views.cart_update_views import *
from apps.shop.views.cart_views import *
from apps.shop.views.product_detail import *
from apps.shop.views.products_store_views import *
from apps.shop.views.shop_views import *

urlpatterns = [
    path('',shop_view,name='shop_view'),
    path('products/',products_store_view,name='products_store_view'),
    path('product-detail/<int:pk>/',shop_product_detail_view,name='shop_product_detail_view'),
    path('product_like/<int:pk>/',product_like,name='product_like'),
    path('product_cheap_like/<int:pk>/',product_cheap_like,name='product_cheap_like'),
    path('search_product/',search_product,name='search_product'),
    path('product_list_results/',product_list_results,name='product_list_results'),
    path('create_product_review/<int:pk>/',create_product_review,name='create_product_review'),
    # product detail add cart 
    path('product-shop_cart_add_product/<int:pk>/',cart_add_product,name='cart_add_product'),
    path('product-shop_cart_remove_product/<int:pk>/',cart_remove_product,name='cart_remove_product'),
    path('product-shop_cart_increment_product/<int:pk>/',cart_increment_product,name='cart_increment_product'),
    path('product-shop_cart_decrement_product/<int:pk>/',cart_decrement_product,name='cart_decrement_product'),
    path('product-shop_cart_message_product/<int:pk>/',cart_message_product,name='cart_message_product'),
    # Cart view
    path('cart_check/',cart_check_view,name='cart_check_view'),
    path('cart_icon_detail/',cart_icon_detail,name='cart_icon_detail'),
    path('shop_cart_view/',shop_cart_view,name='shop_cart_view'),
    path('view-shop_cart_add_view/<int:pk>/',cart_add_view,name='cart_add_view'),
    path('view-shop_cart_remove_view/<int:pk>/',cart_remove_view,name='cart_remove_view'),
    path('view-shop_cart_increment_view/<int:pk>/',cart_increment_view,name='cart_increment_view'),
    path('view-shop_cart_decrement_view/<int:pk>/',cart_decrement_view,name='cart_decrement_view'),
    path('view-shop_cart_message_view/<int:pk>/',cart_message_view,name='cart_message_view'),
    
    
    
    
]

