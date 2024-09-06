from django.urls import path
from apps.products.views.product_review_views import product_review_view

urlpatterns = [
    path('',product_review_view,name='product_review_view'),
]

