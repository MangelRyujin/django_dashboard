from django.urls import path
from apps.products.views.product_review_views import product_active_reviews, product_review_view,product_create_reviews,product_delete_reviews,product_form_update_reviews,product_table_reviews_results,product_update_reviews

urlpatterns = [
    path('',product_review_view,name='product_review_view'),
    path('product_table_reviews_results',product_table_reviews_results,name='product_table_reviews_results'),
    path('product_create_reviews',product_create_reviews,name='product_create_reviews'),
    path('product_update_reviews/<int:pk>/',product_active_reviews,name='product_active_reviews'),
    path('product_form_update_reviews/<int:pk>/',product_form_update_reviews,name='product_form_update_reviews'),
    path('product_delete_reviews/<int:pk>/',product_delete_reviews,name='product_delete_reviews'),
]

