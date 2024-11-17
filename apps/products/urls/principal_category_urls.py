from django.urls import path
from apps.products.views.principal_category_views import *

urlpatterns = [
    path('',principal_category_view,name='principal_category_view'),
    path('principal_category_table_results',principal_category_table_results,name='principal_category_table_results'),
    path('principal_category_detail/<int:pk>/',principal_category_detail,name='principal_category_detail'),
    path('principal_category_create',principal_category_create,name='principal_category_create'),
    path('principal_category_update/<int:pk>/',principal_category_update,name='principal_category_update'),
    path('principal_category_form_update/<int:pk>/',principal_category_form_update,name='principal_category_form_update'),
    path('principal_category_delete/<int:pk>/',principal_category_delete,name='principal_category_delete'),
    
    
]

