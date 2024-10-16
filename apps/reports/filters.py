import django_filters
from apps.sales.models import OrderItem


class ReportOrderItemFilter(django_filters.FilterSet):
    created_date =django_filters.DateFromToRangeFilter(field_name='order__created_date')


    class Meta:
        model = OrderItem
        fields = ['created_date']
        

