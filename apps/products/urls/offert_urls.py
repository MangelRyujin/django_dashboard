from django.urls import path
from apps.products.views.offert_views import *

urlpatterns = [
    path('',offert_view,name='offert_view'),
    path('offert_table_results',offert_table_results,name='offert_table_results'),
    path('offert_detail/<int:pk>/',offert_detail,name='offert_detail'),
    path('offert_create',offert_create,name='offert_create'),
    path('offert_update/<int:pk>/',offert_update,name='offert_update'),
    path('offert_form_update/<int:pk>/',offert_form_update,name='offert_form_update'),
    path('offert_delete/<int:pk>/',offert_delete,name='offert_delete'),
    
    
]

