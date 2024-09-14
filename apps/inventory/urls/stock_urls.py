from django.urls import path
from apps.inventory.views.stock_views import *

urlpatterns = [
    path('',stock_view,name='stock_view'),
    path('stock_table_results',stock_table_results,name='stock_table_results'),
    path('stock_create',stock_create,name='stock_create'),
    path('stock_detail/<int:pk>/',stock_detail,name='stock_detail'),
    path('stock_update/<int:pk>/',stock_update,name='stock_update'),
    path('stock_form_update/<int:pk>/',stock_form_update,name='stock_form_update'),
    path('stock_delete/<int:pk>/',stock_delete,name='stock_delete'),
    
    
]

