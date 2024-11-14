from django.urls import path
from apps.inventory.views.notifications_views import *

urlpatterns = [
    path('',notification_view,name='notification_view'),
    path('notification_empty_view',notification_empty_view,name='notification_empty_view')
]

