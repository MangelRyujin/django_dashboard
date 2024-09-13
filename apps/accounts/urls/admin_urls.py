from django.urls import path
from apps.accounts.views.admin_views.admin_views import *

urlpatterns = [
    path('',admin_view,name='admin_view'),
    path('admin_table_results',admin_table_results,name='admin_table_results'),
    path('admin_detail/<int:pk>/',admin_detail,name='admin_detail'),
    path('admin_create',admin_create,name='admin_create'),
    path('admin_update/<int:pk>/',admin_update,name='admin_update'),
    path('admin_main_information_update/<int:pk>/',admin_main_information_update,name='admin_main_information_update'),
    path('admin_password_update/<int:pk>/',admin_password_update,name='admin_password_update'),
    path('admin_delete/<int:pk>/',admin_delete,name='admin_delete'),
    path('change_information/', change_information, name='change_information'),
]

