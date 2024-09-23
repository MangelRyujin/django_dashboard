from django.urls import path
from apps.sales.views.order_views import *

urlpatterns = [
    path('',order_view,name='order_view'),
    path('order_table_results',order_table_results,name='order_table_results'),
    path('order_detail/<int:pk>/',order_detail,name='order_detail')
    
]

