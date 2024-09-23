from django.urls import path
from apps.sales.views.order_settings_views import *

urlpatterns = [
    path('',order_settings_view,name='order_settings_view')
]

