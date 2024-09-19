from django.urls import path
from apps.inventory.views.stock_movements_views import *

urlpatterns = [
    path('',stock_movements_view,name='stock_movements_view'),
    path('stock_movements_table_results',stock_movements_table_results,name='stock_movements_table_results'),
    path('stock_movements_simple_create',stock_movements_simple_create,name='stock_movements_simple_create'),
    path('stock_movements_multiple_create',stock_movements_multiple_create,name='stock_movements_multiple_create'),
    path('stock_movements_detail/<int:pk>/',stock_movements_detail,name='stock_movements_detail'),
    
    
]

