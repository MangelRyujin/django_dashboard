from django.shortcuts import render
import logging
from django.contrib.admin.views.decorators import staff_member_required
logger = logging.getLogger(__name__)

# order view (index)
@staff_member_required(login_url='/shop')
def order_settings_view(request):
    response= render(request,'sales/order_settings_templates/settings.html')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
