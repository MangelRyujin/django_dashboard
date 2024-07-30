from django.urls import path
from apps.products.views.product_views import *

urlpatterns = [
    path('',product_view,name='product_view'),
    path('product_table_results',product_table_results,name='product_table_results'),
    path('product_detail/<int:pk>/',product_detail,name='product_detail'),
    path('product_create',product_create,name='product_create'),
    path('product_update/<int:pk>/',product_update,name='product_update'),
    path('product_form_update/<int:pk>/',product_form_update,name='product_form_update'),
    path('product_delete/<int:pk>/',product_delete,name='product_delete'),
    
    
]

