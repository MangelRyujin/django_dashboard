from django.urls import path
from apps.sales.views.local_order_views import *

urlpatterns = [
    path('',local_order_view,name='local_order_view'),
    path('local_order_results_view',local_order_results_view,name='local_order_results_view'),
    path('local_order_detail/<int:pk>/',local_order_detail,name='local_order_detail'),
    path('local_order_create',local_order_create,name='local_order_create'),
    path('local_order_item_create/<int:pk>/',local_order_item_create,name='local_order_item_create'),
    path('local_order_item_stock_create/<int:pk>/',local_order_item_stock_create,name='local_order_item_stock_create'),
    path('local_order_delete/<int:pk>/',local_order_delete,name='local_order_delete'),
    path('local_order_delete_sold/<int:pk>/',local_order_delete_sold,name='local_order_delete_sold'),
    path('local_order_item_stock_delete/<int:pk>/',local_order_item_stock_delete,name='local_order_item_stock_delete'),
    path('local_order_item_delete/<int:pk>/',local_order_item_delete,name='local_order_item_delete'),
    path('local_order_check_revert/<int:pk>/',local_order_check_revert,name='local_order_check_revert'),
    path('local_order_update/<int:pk>/',local_order_update,name='local_order_update'),
    path('local_order_form_update/<int:pk>/',local_order_form_update,name='local_order_form_update'),
    path('local_order_sold/<int:pk>/',local_order_sold,name='local_order_sold'),
]

