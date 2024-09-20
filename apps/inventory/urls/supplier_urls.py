from django.urls import path
from apps.inventory.views.supplier_views import *

urlpatterns = [
    path('',supplier_view,name='supplier_view'),
    path('supplier_table_results',supplier_table_results,name='supplier_table_results'),
    path('supplier_detail/<int:pk>/',supplier_detail,name='supplier_detail'),
    path('supplier_create',supplier_create,name='supplier_create'),
    path('supplier_update/<int:pk>/',supplier_update,name='supplier_update'),
    path('supplier_form_update/<int:pk>/',supplier_form_update,name='supplier_form_update'),
    path('supplier_delete/<int:pk>/',supplier_delete,name='supplier_delete'),

]

