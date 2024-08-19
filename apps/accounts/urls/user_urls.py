from django.urls import path
from apps.accounts.views.users_views.user_views import *

urlpatterns = [
    path('',user_view,name='user_view'),
    path('user_table_results',user_table_results,name='user_table_results'),
    
    
]

