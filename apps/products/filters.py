import django_filters

from apps.products.models import Category

class CategoryFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    class Meta:
        model = Category
        fields = ['name','is_active']