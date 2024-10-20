from django.urls import path
from apps.sales.views.local_order_views import *
from apps.sales.views.shop_order_views import *

urlpatterns = [
    path('',shop_order_view,name='shop_order_view'),
    path('shop_order_results_view',shop_order_results_view,name='shop_order_results_view'),
    path('shop_order_detail/<int:pk>/',shop_order_detail,name='shop_order_detail'),
    path('local_order_create',local_order_create,name='local_order_create'),
    path('shop_order_item_update/<int:pk>/',shop_order_item_update,name='shop_order_item_update'),
    path('local_order_item_stock_create/<int:pk>/',local_order_item_stock_create,name='local_order_item_stock_create'),
    path('shop_order_delete/<int:pk>/',shop_order_delete,name='shop_order_delete'),
    path('local_order_delete_sold/<int:pk>/',local_order_delete_sold,name='local_order_delete_sold'),
    path('local_order_item_stock_delete/<int:pk>/',local_order_item_stock_delete,name='local_order_item_stock_delete'),
    path('shop_order_item_delete/<int:pk>/',shop_order_item_delete,name='shop_order_item_delete'),
    path('local_order_check_revert/<int:pk>/',local_order_check_revert,name='local_order_check_revert'),
    path('shop_order_update/<int:pk>/',shop_order_update,name='shop_order_update'),
    path('shop_order_form_update/<int:pk>/',shop_order_form_update,name='shop_order_form_update'),
    path('local_order_sold/<int:pk>/',local_order_sold,name='local_order_sold'),
]

