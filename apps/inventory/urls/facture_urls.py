from django.urls import path
from apps.inventory.views.facture_views import *

urlpatterns = [
    path('',facture_view,name='facture_view'),
    path('facture_table_results',facture_table_results,name='facture_table_results'),
    path('facture_detail/<int:pk>/',facture_detail,name='facture_detail'),
    path('facture_create',facture_create,name='facture_create'),
    path('facture_update/<int:pk>/',facture_update,name='facture_update'),
    path('facture_form_update/<int:pk>/',facture_form_update,name='facture_form_update'),
    path('facture_delete/<int:pk>/',facture_delete,name='facture_delete'),
    
    
]

