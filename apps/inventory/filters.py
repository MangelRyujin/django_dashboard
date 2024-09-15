import django_filters
from apps.inventory.models import CategoryStock, Stock,Warehouse

class CategoryStockFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = CategoryStock
        fields = ['name']

class WarehouseFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    address=  django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Warehouse
        fields = ['name','address']
        
class StockFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    address=  django_filters.CharFilter(lookup_expr='icontains')
    code=  django_filters.CharFilter(lookup_expr='icontains')
    address=  django_filters.CharFilter(lookup_expr='icontains')
    product=  django_filters.CharFilter(field_name='product__name',lookup_expr='icontains')
    warehouse = django_filters.ModelMultipleChoiceFilter(queryset=Warehouse.objects.all())
    categories = django_filters.ModelMultipleChoiceFilter(queryset=CategoryStock.objects.all())
    is_active = django_filters.BooleanFilter()
    measure_unit=  django_filters.CharFilter(lookup_expr='exact')
    
    class Meta:
        model = Stock
        fields = ['code','name','product','address','warehouse','categories','is_active','measure_unit']