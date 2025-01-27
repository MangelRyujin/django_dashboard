import django_filters
from apps.accounts.models import User
from apps.inventory.models import Warehouse
from apps.products.models import Product
from apps.sales.models import LocalOrder, Order, Shift


class OrderFilter(django_filters.FilterSet):
    user_create=django_filters.ModelMultipleChoiceFilter(queryset=User.objects.filter(is_staff=True))
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
        fields = ['id','user_create','user_full_name','product','user_phone','payment_type','user_ci','created_date','type']
    
    def filter_by_product(self, qs, name, value):
        return qs.filter(orderitem__product_id=value)
        

class LocalOrderFilter(django_filters.FilterSet):
    user_create=django_filters.ModelMultipleChoiceFilter(queryset=User.objects.filter(is_staff=True))
    user_full_name = django_filters.CharFilter(lookup_expr='icontains')
    user_phone = django_filters.CharFilter(lookup_expr='icontains')
    user_ci = django_filters.CharFilter(lookup_expr='icontains')
    created_date =django_filters.DateFromToRangeFilter()
    id = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = LocalOrder
        fields = ['id','user_create','user_first_name','user_last_name','user_phone','user_ci','created_date']
        
class ShiftFilter(django_filters.FilterSet):
    warehouse=django_filters.ModelMultipleChoiceFilter(queryset=Warehouse.objects.all())
    create_user_username = django_filters.CharFilter(lookup_expr='icontains')
   
    create_date_at =django_filters.DateFromToRangeFilter()
    pk = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Shift
        fields = ['pk','create_user_username','warehouse','create_date_at']