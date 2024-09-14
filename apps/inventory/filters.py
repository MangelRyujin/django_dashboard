import django_filters
from apps.inventory.models import CategoryStock,Wharehouse

class CategoryStockFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = CategoryStock
        fields = ['name']

class WharehouseFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Wharehouse
        fields = ['name']