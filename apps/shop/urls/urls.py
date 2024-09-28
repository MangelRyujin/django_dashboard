from django.urls import path
from apps.shop.views.products_store_views import *
from apps.shop.views.shop_views import *

urlpatterns = [
    path('',shop_view,name='shop_view'),
    path('products/',products_store_view,name='products_store_view'),
    
]

