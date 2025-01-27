from django.shortcuts import render
from apps.accounts.models import User
from apps.products.models import Product
from apps.sales.filters import OrderFilter
from django.core.paginator import Paginator
import logging
from django.contrib.admin.views.decorators import staff_member_required
from apps.sales.models import Order,OrderItem
logger = logging.getLogger(__name__)

# order view (index)
@staff_member_required(login_url='/')
def order_view(request):
    products=Product.objects.all()
    created_users = User.objects.filter(is_staff=True)
    response= render(request,'sales/order_templates/order.html',{"products":products,"created_users":created_users})
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response

# Charge result table
@staff_member_required(login_url='/')
def order_table_results(request):
    return  render(request,'sales/order_templates/order_table_results.html',context=_show_order(request))


# Show order table
@staff_member_required(login_url='/')
def _show_order(request):
    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    orders = OrderFilter(request.GET, queryset=Order.objects.all().order_by('-id'))
    paginator = Paginator(orders.qs, 25)    # Show 25 contacts per page.
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    context={
        
        'pagination':page_obj,
        'parameters': parameters,
    }
    return context


# Detail user order table
@staff_member_required(login_url='/')
def order_detail(request,pk):
    order = Order.objects.filter(pk=pk).first()
    items = order.orderitem_set.all()
    return  render(request,'sales/order_templates/actions/orderDetail/orderDetail.html',{"order":order,"items":items})
     