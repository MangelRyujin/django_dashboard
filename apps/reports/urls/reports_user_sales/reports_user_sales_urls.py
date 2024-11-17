from django.urls import path
from apps.reports.views.reports_products_sales.reports_product_user_sales import *

urlpatterns = [
    path('',reports_user_sales_view,name='reports_user_sales_view'),
    path('reports_user_sales_view_results',reports_user_sales_view_results,name='reports_user_sales_view_results'),
    
]

