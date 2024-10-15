from django.urls import path
from apps.general.views.charts.dashboard.chart import *
from apps.general.views.settings_views import *

urlpatterns = [
    path('get_total_items_orders/',get_total_items_orders,name='get_total_items_orders'),
    path('get_total_price_orders/',get_total_price_orders,name='get_total_price_orders'),
    path('get_total_items_orders_month/<int:year>/',get_total_items_orders_month,name='get_total_items_orders_month'),
    path('get_total_items_orders_price_month/<int:year>/',get_total_items_orders_price_month,name='get_total_items_orders_price_month'),
    
    
]

