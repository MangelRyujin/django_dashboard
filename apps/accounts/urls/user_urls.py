from django.urls import path
from apps.accounts.views.users_views.user_views import *

urlpatterns = [
    path('',user_view,name='user_view'),
    path('user_table_results',user_table_results,name='user_table_results'),
    path('user_detail/<int:pk>/',user_detail,name='user_detail'),
    path('user_update/<int:pk>/',user_update,name='user_update'),
    path('user_password_update/<int:pk>/',user_password_update,name='user_password_update'),
    path('user_delete/<int:pk>/',user_delete,name='user_delete'),
    
    
]

