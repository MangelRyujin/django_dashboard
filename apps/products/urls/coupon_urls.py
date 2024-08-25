from django.urls import path
from apps.products.views.coupon_views import *

urlpatterns = [
    path('',coupon_view,name='coupon_view'),
    path('coupon_table_results',coupon_table_results,name='coupon_table_results'),
    path('coupon_create',coupon_create,name='coupon_create'),
    path('coupon_update/<str:pk>/',coupon_update,name='coupon_update'),
    path('coupon_form_update/<str:pk>/',coupon_form_update,name='coupon_form_update'),
    path('coupon_delete/<str:pk>/',coupon_delete,name='coupon_delete'),
    
    
]

