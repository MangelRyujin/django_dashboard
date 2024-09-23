import django_filters
from apps.products.models import Product
from apps.sales.models import Order


class OrderFilter(django_filters.FilterSet):
    user_full_name = django_filters.CharFilter(lookup_expr='icontains')
    user_phone = django_filters.CharFilter(lookup_expr='icontains')
    product = django_filters.CharFilter(
        method='filter_by_product',
        lookup_expr='exact'
    )
    user_ci = django_filters.CharFilter(lookup_expr='icontains')
    created_date =django_filters.DateFromToRangeFilter()
    id = django_filters.CharFilter(lookup_expr='icontains')
    type =  django_filters.CharFilter(lookup_expr='exact')
    payment_type =  django_filters.CharFilter(lookup_expr='exact')


    class Meta:
        model = Order
        fields = ['id','user_full_name','product','user_phone','payment_type','user_ci','created_date','type']
    
    def filter_by_product(self, qs, name, value):
        return qs.filter(orderitem__product_id=value)
        