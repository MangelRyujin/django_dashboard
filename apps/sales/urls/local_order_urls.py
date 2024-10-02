from django.urls import path
from apps.sales.views.local_order_views import *

urlpatterns = [
    path('',local_order_view,name='local_order_view'),
    path('local_order_results_view',local_order_results_view,name='local_order_results_view'),
    path('local_order_create',local_order_create,name='local_order_create'),
    path('local_order_delete/<int:pk>/',local_order_delete,name='local_order_delete'),
    path('local_order_check/<int:pk>/',local_order_check,name='local_order_check'),
    
    
    
    
]

