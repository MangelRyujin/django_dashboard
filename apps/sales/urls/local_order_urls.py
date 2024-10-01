from django.urls import path
from apps.sales.views.local_order_views import *

urlpatterns = [
    path('',local_order_view,name='local_order_view'),
    path('local_order_results_view',local_order_results_view,name='local_order_results_view'),
    
    
]

