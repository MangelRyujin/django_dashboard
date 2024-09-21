import django_filters
from apps.accounts.models import User
from apps.inventory.models import CategoryStock, Facture, Stock, StockMovements, Supplier,Warehouse
from django.utils import timezone


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
    
class StockMovementFilter(django_filters.FilterSet):
    type =  django_filters.CharFilter(lookup_expr='exact')
    movement_type =  django_filters.CharFilter(lookup_expr='exact')
    stock_one=  django_filters.CharFilter(field_name='stock_one__name',lookup_expr='icontains')
    stock_two=  django_filters.CharFilter(field_name='stock_two__name',lookup_expr='icontains')
    user=  django_filters.CharFilter(field_name='user__username',lookup_expr='icontains')
    motive=  django_filters.CharFilter(lookup_expr='icontains')
    created_date =django_filters.DateFromToRangeFilter()

    
    class Meta:
        model = StockMovements
        fields = ['type','movement_type','stock_one','stock_two','user','motive','created_date']
        
class SupplierFilter(django_filters.FilterSet):
    ci =  django_filters.CharFilter(lookup_expr='icontains')
    first_name =  django_filters.CharFilter(lookup_expr='icontains')
    last_name =  django_filters.CharFilter(lookup_expr='icontains')
    email =  django_filters.CharFilter(lookup_expr='icontains')
    phone_number =  django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Supplier
        fields = ['ci','first_name','last_name','email','phone_number']
        

class FactureFilter(django_filters.FilterSet):
    product=  django_filters.CharFilter(field_name='product__name',lookup_expr='icontains')
    measure_unit=  django_filters.CharFilter(lookup_expr='exact')
    supplier = django_filters.ModelMultipleChoiceFilter(queryset=Supplier.objects.all())
    code=  django_filters.CharFilter(lookup_expr='icontains')
    created_date =django_filters.DateFromToRangeFilter()

    
    class Meta:
        model = Facture
        fields = ['product','measure_unit','supplier','code','created_date']