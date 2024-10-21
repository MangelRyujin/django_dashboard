from django.urls import path
from apps.sales.views.shop_order_views import *

urlpatterns = [
    path('',shop_order_view,name='shop_order_view'),
    path('shop_order_results_view',shop_order_results_view,name='shop_order_results_view'),
    path('shop_order_detail/<int:pk>/',shop_order_detail,name='shop_order_detail'),
    path('shop_order_item_update/<int:pk>/',shop_order_item_update,name='shop_order_item_update'),
    path('shop_order_item_stock_create/<int:pk>/',shop_order_item_stock_create,name='shop_order_item_stock_create'),
    path('shop_order_delete/<int:pk>/',shop_order_delete,name='shop_order_delete'),
    path('shop_order_delete_sold/<int:pk>/',shop_order_delete_sold,name='shop_order_delete_sold'),
    path('shop_order_item_stock_delete/<int:pk>/',shop_order_item_stock_delete,name='shop_order_item_stock_delete'),
    path('shop_order_item_delete/<int:pk>/',shop_order_item_delete,name='shop_order_item_delete'),
    path('shop_order_check_revert/<int:pk>/',shop_order_check_revert,name='shop_order_check_revert'),
    path('shop_order_update/<int:pk>/',shop_order_update,name='shop_order_update'),
    path('shop_order_form_update/<int:pk>/',shop_order_form_update,name='shop_order_form_update'),
    path('shop_order_sold/<int:pk>/',shop_order_sold,name='shop_order_sold'),
]

