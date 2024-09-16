from django.urls import path
from apps.inventory.views.stock_movements_views import *

urlpatterns = [
    path('',stock_movements_view,name='stock_movements_view'),
    path('stock_movements_table_results',stock_movements_table_results,name='stock_movements_table_results'),
    path('stock_movements_create',stock_movements_create,name='stock_movements_create'),
    path('stock_movements_detail/<int:pk>/',stock_movements_detail,name='stock_movements_detail'),
    path('stock_movements_update/<int:pk>/',stock_movements_update,name='stock_movements_update'),
    path('stock_movements_form_update/<int:pk>/',stock_movements_form_update,name='stock_movements_form_update'),
    path('stock_movements_delete/<int:pk>/',stock_movements_delete,name='stock_movements_delete'),
    
    
]

