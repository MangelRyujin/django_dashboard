from django.urls import path
from apps.inventory.views.spent_views import *

urlpatterns = [
    path('',spent_view,name='spent_view'),
    path('spent_table_results',spent_table_results,name='spent_table_results'),
    path('spent_detail/<int:pk>/',spent_detail,name='spent_detail'),
    path('spent_create',spent_create,name='spent_create'),
    path('spent_update/<int:pk>/',spent_update,name='spent_update'),
    path('spent_form_update/<int:pk>/',spent_form_update,name='spent_form_update'),
    path('spent_delete/<int:pk>/',spent_delete,name='spent_delete'),
]

