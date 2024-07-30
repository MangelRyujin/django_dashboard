import django_filters

from apps.products.models import Category, Product

class CategoryFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    class Meta:
        model = Category
        fields = ['name','is_active']
        

class ProductFilter(django_filters.FilterSet):
    code=  django_filters.CharFilter(lookup_expr='icontains')
    name=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    stars = django_filters.NumberFilter()
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['code','name','is_active','stars','categories']