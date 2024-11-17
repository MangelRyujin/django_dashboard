import django_filters
from apps.inventory.models import Facture, Income, Spent
from apps.sales.models import *


class ReportOrderItemFilter(django_filters.FilterSet):
    created_date =django_filters.DateFromToRangeFilter(field_name='order__created_date')


    class Meta:
        model = OrderItem
        fields = ['created_date']
        

class ReportOrderFilter(django_filters.FilterSet):
    created_date =django_filters.DateFromToRangeFilter(field_name='created_date')


    class Meta:
        model = Order
        fields = ['created_date']
        

class ReportFactureFilter(django_filters.FilterSet):
    created_date =django_filters.DateFromToRangeFilter(field_name='created_date')


    class Meta:
        model = Facture
        fields = ['created_date']
        

class ReportIncomeFilter(django_filters.FilterSet):
    created_date =django_filters.DateFromToRangeFilter(field_name='created_date')


    class Meta:
        model = Income
        fields = ['created_date']
        

class ReportSpentFilter(django_filters.FilterSet):
    created_date =django_filters.DateFromToRangeFilter(field_name='created_date')


    class Meta:
        model = Spent
        fields = ['created_date']
        
class ReportUsersOrderItemFilter(django_filters.FilterSet):
    created_date =django_filters.DateFromToRangeFilter(field_name='order__created_date')
    user = django_filters.CharFilter(field_name='order__user_create__pk',lookup_expr='exact')

    class Meta:
        model = OrderItem
        fields = ['created_date','user']

class ReportUserOrderFilter(django_filters.FilterSet):
    created_date =django_filters.DateFromToRangeFilter(field_name='created_date')
    user = django_filters.CharFilter(field_name='user_create__pk',lookup_expr='exact')

    class Meta:
        model = Order
        fields = ['created_date','user']