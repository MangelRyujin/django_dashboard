from django.urls import path
from apps.products.views.category_views import *

urlpatterns = [
    path('',category_view,name='category_view'),
    path('category_table_results',category_table_results,name='category_table_results'),
    path('category_detail/<int:pk>/',category_detail,name='category_detail'),
    path('category_create',category_create,name='category_create'),
    path('category_update/<int:pk>/',category_update,name='category_update'),
    path('category_form_update/<int:pk>/',category_form_update,name='category_form_update'),
    path('category_delete/<int:pk>/',category_delete,name='category_delete'),
    
    
]

