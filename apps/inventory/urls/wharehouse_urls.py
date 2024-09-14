from django.urls import path
from apps.inventory.views.wharehouse_views import *

urlpatterns = [
    path('',wharehouse_view,name='wharehouse_view'),
    path('wharehouse_table_results',wharehouse_table_results,name='wharehouse_table_results'),
    path('wharehouse_create',wharehouse_create,name='wharehouse_create'),
    path('wharehouse_update/<int:pk>/',wharehouse_update,name='wharehouse_update'),
    path('wharehouse_form_update/<int:pk>/',wharehouse_form_update,name='wharehouse_form_update'),
    path('wharehouse_delete/<int:pk>/',wharehouse_delete,name='wharehouse_delete'),
    
    
]

