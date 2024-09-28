import django_filters

from apps.accounts.models import User
from apps.products.models import Category, Offert, Product,Coupon,ProductReview

class CategoryFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    class Meta:
        model = Category
        fields = ['name','is_active']
        
class OffertFilter(django_filters.FilterSet):
    name=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    init_date =django_filters.DateTimeFilter(lookup_expr='gte')
    end_date =django_filters.DateFromToRangeFilter(lookup_expr='lte')
    class Meta:
        model = Offert
        fields = ['name','is_active','init_date','end_date']
        

class ProductFilter(django_filters.FilterSet):
    code=  django_filters.CharFilter(lookup_expr='icontains')
    name=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    stars = django_filters.NumberFilter()
    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['code','name','is_active','stars','categories']
        
        
class CouponFilter(django_filters.FilterSet):
    code=  django_filters.CharFilter(lookup_expr='icontains')
    is_active = django_filters.BooleanFilter()
    is_exhausted = django_filters.BooleanFilter()
    user = django_filters.ModelMultipleChoiceFilter(queryset=User.objects.all())
    product = django_filters.ModelMultipleChoiceFilter(queryset=Product.objects.all())
    class Meta:
        model = Coupon
        fields = ['code','is_active','is_exhausted','user','product']

class ProductReviewFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='user__username',lookup_expr='icontains')
    product = django_filters.ModelMultipleChoiceFilter(queryset=Product.objects.all())
    stars = django_filters.NumberFilter()
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = ProductReview
        fields = ['username','product','stars','is_active',]
    