from django.urls import path
from apps.inventory.views.income_views import *

urlpatterns = [
    path('',income_view,name='income_view'),
    path('income_table_results',income_table_results,name='income_table_results'),
    path('income_detail/<int:pk>/',income_detail,name='income_detail'),
    path('income_create',income_create,name='income_create'),
    path('income_update/<int:pk>/',income_update,name='income_update'),
    path('income_form_update/<int:pk>/',income_form_update,name='income_form_update'),
    path('income_delete/<int:pk>/',income_delete,name='income_delete'),
]

