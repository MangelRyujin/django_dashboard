import django_filters
from django.contrib.auth.models import Group
from apps.accounts.models import User


class AdminFilter(django_filters.FilterSet):
    email=  django_filters.CharFilter(lookup_expr='icontains')
    username=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    is_staff = django_filters.BooleanFilter()
    groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all())


    class Meta:
        model = User
        fields = ['email','groups','username','is_active','is_staff']

            
class UserFilter(django_filters.FilterSet):
    email=  django_filters.CharFilter(lookup_expr='icontains')
    username=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    is_staff = django_filters.BooleanFilter()
    


    class Meta:
        model = User
        fields = ['email','username','is_active','is_staff']

            