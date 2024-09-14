from django.urls import path
from apps.inventory.views.warehouse_views import *

urlpatterns = [
    path('',warehouse_view,name='warehouse_view'),
    path('warehouse_table_results',warehouse_table_results,name='warehouse_table_results'),
    path('warehouse_create',warehouse_create,name='warehouse_create'),
    path('warehouse_update/<int:pk>/',warehouse_update,name='warehouse_update'),
    path('warehouse_form_update/<int:pk>/',warehouse_form_update,name='warehouse_form_update'),
    path('warehouse_delete/<int:pk>/',warehouse_delete,name='warehouse_delete'),
    
    
]

