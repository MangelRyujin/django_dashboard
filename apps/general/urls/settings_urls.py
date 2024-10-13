from django.urls import path
from apps.general.views.settings_views import *

urlpatterns = [
    path('',settings_view,name='settings_view'),
    path('save_header_settings_view',save_header_settings_view,name='save_header_settings_view'),
    path('save_local_settings_view',save_local_settings_view,name='save_local_settings_view'),
    path('save_shop_settings_view',save_shop_settings_view,name='save_shop_settings_view'),
    path('save_social_settings_view',save_social_settings_view,name='save_social_settings_view'),
    path('save_wapp_settings_view',save_wapp_settings_view,name='save_wapp_settings_view'),
    path('save_goal_settings_view',save_goal_settings_view,name='save_goal_settings_view'),
    
]

