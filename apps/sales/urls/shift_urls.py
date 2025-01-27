from django.urls import path
from apps.sales.views.shift_views import *

urlpatterns = [
    path('',shift_view ,name='shift_view'),
    path('shift_table_results',shift_table_results,name='shift_table_results'),
    path('shift_detail/<int:pk>/',shift_detail,name='shift_detail'),
    path('shift_create',shift_create,name='shift_create'),
    # path('shift_update/<int:pk>/',shift_update,name='shift_update'),
    path('shift_form_update/<int:pk>/',shift_form_update,name='shift_form_update'),
    path('shift_delete/<int:pk>/',shift_delete,name='shift_delete'),
    path('shift_report_detail/<int:pk>/',shift_report_detail,name='shift_report_detail'),
    path('shift_close_report/<int:pk>/',shift_close_report,name='shift_close_report'),
    
    
]

