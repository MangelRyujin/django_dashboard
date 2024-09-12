from django.urls import path
from apps.inventory.views.category_stock_views import *

urlpatterns = [
    path('',category_stock_view,name='category_stock_view'),
    path('category_stock_table_results',category_stock_table_results,name='category_stock_table_results'),
    path('category_stock_detail/<int:pk>/',category_stock_detail,name='category_stock_detail'),
    path('category_stock_create',category_stock_create,name='category_stock_create'),
    path('category_stock_update/<int:pk>/',category_stock_update,name='category_stock_update'),
    path('category_stock_form_update/<int:pk>/',category_stock_form_update,name='category_stock_form_update'),
    path('category_stock_delete/<int:pk>/',category_stock_delete,name='category_stock_delete'),
    
    
]

