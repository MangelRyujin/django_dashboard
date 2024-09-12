import django_filters

from apps.accounts.models import User
from apps.inventory.models import CategoryStock

class CategoryStockFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = CategoryStock
        fields = ['name']